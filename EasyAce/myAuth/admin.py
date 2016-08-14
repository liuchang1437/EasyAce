from django.contrib import admin
from django.http import HttpResponse
from .models import Tutor,Student,MyUser,Feedback,\
  StudentPreferSub,PreferSubject,ReferSubject,Interview,\
  StudentIntent,OptionalTutor
import xlwt
from django.utils.html import format_html
from django.core.urlresolvers import reverse
# Register your models here.
# class RecordInline(admin.StackedInline):
#   colapse = True
#   model = Record
#   extra = 0
#   raw_id_fields = ('tutor',)
#   fieldsets = (
#     ('Record info',{
#       'fields':('tutor',('if_confirmed','successful_match','commission_collection_status'))
#     }),
#     ('Contract and fees',{
#       'fields':('startdate','chargedate','service_fees','freq','lesson_last','lesson_price')
#     }),
#     ('Close call',{
#       'classes':('collapse',),
#       'fields':('close_call_date','tuition_duration','overall_comment','q1','q2','self_evaluation',\
#         'reasons','comment_charges','recommend_or_not')
#     })
#   )
class OptionalTutorInline(admin.StackedInline):
  extra = 0
  model = OptionalTutor
  raw_id_fields = ['tutor',]
class FeedbackInline(admin.StackedInline):
  def has_add_permission(self,request):
    return False
  model = Feedback
  extra = 0
  raw_id_fields = ['tutor',]
class IntentInTutorInline(admin.StackedInline):
  def has_add_permission(self,request):
    return False
  verbose_name = 'Record'
  verbose_name_plural = 'Records'
  model = StudentIntent
  readonly_fields = ['intent_link',]
  fields = ('intent_link',)
  def intent_link(self, instance):
    if instance:
        fk_id = instance.id
    else:
        fk_id = None
    if fk_id:
        intent = StudentIntent.objects.get(pk=fk_id)
        opts = intent._meta
        related_url = reverse('admin:%s_%s_change' %(opts.app_label,  \
          opts.model_name),  args=[fk_id] )
        return format_html(
              '<a target=_blank href="{}">{}</a>', related_url,intent.student.full_name)
    else:
        return "Record not exists."
  intent_link.short_description = "A record with"

class IntentInStudentInline(admin.StackedInline):
  def has_add_permission(self,request):
    return False
  verbose_name = "intent"
  verbose_name_plural = "Student's intents"
  model = StudentIntent
  readonly_fields = ['intent_link',]
  fields = ('intent_link',)
  def intent_link(self, instance):
    if instance:
        fk_id = instance.id
    else:
        fk_id = None
    if fk_id:
        intent = StudentIntent.objects.get(pk=fk_id)
        opts = intent._meta
        related_url = reverse('admin:%s_%s_change' %(opts.app_label,  \
          opts.model_name),  args=[fk_id] )
        return format_html(
              '<a target=_blank href="{}">Check this record</a>', related_url)
    else:
        return "Record not exists."
  intent_link.short_description = "Record link"

class InterviewInline(admin.StackedInline):
  colapse = True
  model = Interview
  extra = 0
  raw_id_fields = ('tutor',)
  fieldsets = (
    ('Interview Form',{
      'classes':('collapse',),
      'fields':('interview_presentability','interview_friendliness','interview_crisis_hand',\
        'interview_communication','interview_grade',\
    'interview_major','interview_num_taught','interview_effect','interview_fees','interview_how_to_range_course',\
    'interview_tutor_type','interview_why_you_good','interview_how_relation_with_stu','interview_how_rel_with_prntofstu',\
    'interview_how_long','interview_why_tutor','interview_what_matter','interview_other_sub','interview_can_teach_tutor',\
    'interview_recommend','interview_new_tutor_training','interview_comment','interview_remark')
    }),
  )
  radio_fields = {
    'interview_presentability':admin.HORIZONTAL,
    'interview_friendliness':admin.HORIZONTAL,
    'interview_crisis_hand':admin.HORIZONTAL,
    'interview_communication':admin.HORIZONTAL
  }

class PreferSub(admin.StackedInline):
  def has_add_permission(self,request):
    return False
  can_delete = False
  model = PreferSubject
  fields = ('level','name')
  #readonly_fields = ('level','name')
class ReferSub(admin.StackedInline):
  def has_add_permission(self,request):
    return False
  can_delete = False
  model = ReferSubject
  fields = ('level','name','score')
  # readonly_fields = ('level','name','score')


@admin.register(Tutor) 
class TutorAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
        return False
  # def colored_name(self,obj):
  #       return '<span style="color: #123456;">{} {}</span>'.format(obj.first_name,obj.last_name)
 
  # colored_name.allow_tags = True
  list_display = ('full_name','username_link','gender','school','phone','wechat','whatsapp')
  list_filter = ('check','top_teacher','prefer_sub__level','prefer_sub__name')
  search_fields = ('full_name','username','email','prefer_sub__level','prefer_sub__name','interview__interview_grade',\
    'interview__interview_major','interview__interview_num_taught','interview__interview_effect','interview__interview_fees','interview__interview_how_to_range_course',\
    'interview__interview_tutor_type','interview__interview_why_you_good','interview__interview_how_relation_with_stu','interview__interview_how_rel_with_prntofstu',\
    'interview__interview_how_long','interview__interview_why_tutor','interview__interview_what_matter','interview__interview_other_sub','interview__interview_can_teach_tutor',\
    'interview__interview_recommend','interview__interview_new_tutor_training','interview__interview_comment','interview__interview_remark')
  fieldsets = (
    ('Personal information', {
      'fields': ('full_name','gender','birth','school',\
        'phone','wechat','whatsapp','email','tutor_location1',\
        'tutor_location2','tutor_location3','teach_duration',\
        'num_taught','achievement','sr','signup_datetime','last_edit_time')
    }),
    ('Options',{
      'fields':('check','top_teacher')
    })
  ) 
  
  readonly_fields = ('signup_datetime','last_edit_time')
  # readonly_fields = ('name','username','gender','birth','school',\
  #   'tutor_location1','tutor_location2','tutor_location3',\
  #   'teach_duration','num_taught','achievement','phone',\
  #   'wechat','whatsapp','email','sr')
  inlines = [PreferSub,ReferSub,InterviewInline,IntentInTutorInline]
  # 增加计算Star rating的action
  def cal_star_rating(self,request,queryset):
    for obj in queryset:
      obj.cal_sr()
      obj.save()
    self.message_user(request,'Successfully updated star-ratings of the selected tutors!')
  cal_star_rating.short_description = 'Update the star rating'
  # end
  
  # 导出到excel文件的action
  def export_to_excel(self,request,queryset):
    response = HttpResponse()
    response['Content-Type'] = 'application/vnd.ms-excel'
    response['Content-Disposition'] = 'attachment;filename=tutors_information.xls'
    wb = xlwt.Workbook(encoding = 'utf-8')
    sheet = wb.add_sheet('tutors')
    sheet.write(0,0,'full_name')
    sheet.write(0,1,'username')
    sheet.write(0,2,'gender')
    sheet.write(0,3,'email')
    sheet.write(0,4,'phone')
    sheet.write(0,5,'school')
    sheet.write(0,6,'wechat')
    sheet.write(0,7,'whatsapp')
    sheet.write(0,8,'phone')
    sheet.write(0,9,'tutor_location1')
    sheet.write(0,10,'tutor_location2')
    sheet.write(0,11,'tutor_location3')
    sheet.write(0,12,'teach_duration')
    sheet.write(0,13,'num_taught')
    sheet.write(0,14,'achievement')
    sheet.write(0,15,'star rating')
    sheet.write(0,16,'prefer subject1')
    sheet.write(0,17,'prefer subject2')
    sheet.write(0,18,'prefer subject3')
    sheet.write(0,19,'prefer subject4')
    sheet.write(0,20,'refer subject1')
    sheet.write(0,21,'refer subject2')
    sheet.write(0,22,'refer subject3')
    sheet.write(0,23,'refer subject4')
    row = 1
    for tutor in queryset:
      sheet.write(row,0,tutor.full_name)
      sheet.write(row,1,tutor.username)
      sheet.write(row,2,tutor.gender)
      sheet.write(row,3,tutor.email)
      sheet.write(row,4,tutor.phone)
      sheet.write(row,5,tutor.school)
      sheet.write(row,6,tutor.wechat)
      sheet.write(row,7,tutor.whatsapp)
      sheet.write(row,8,tutor.phone)
      sheet.write(row,9,tutor.tutor_location1)
      sheet.write(row,10,tutor.tutor_location2)
      sheet.write(row,11,tutor.tutor_location3)
      sheet.write(row,12,tutor.teach_duration)
      sheet.write(row,13,tutor.num_taught)
      sheet.write(row,14,tutor.achievement)
      sheet.write(row,15,tutor.sr)
      prefer_subs = []
      for sub in tutor.prefer_subs.all():
        prefer_subs.append(sub.level+','+sub.name)
      refer_subs = []
      for sub in tutor.refer_subs.all():
        refer_subs.append(sub.level+','+sub.name+','+sub.score)
      for index in range(0,min(4,len(prefer_subs))):
        sheet.write(row,16+index,prefer_subs[index])
      for index in range(0,min(4,len(refer_subs))):
        sheet.write(row,20+index,prefer_subs[index])
      row+=1
      # end for
    wb.save(response)
    return response
  # end
  export_to_excel.short_description = 'Export to excel'
  def username_link(self, instance):
        if instance:
            fk_id = instance.id
        else:
            fk_id = None
        if fk_id:
            tutor = instance
            opts = tutor._meta
            related_url = reverse('admin:%s_%s_change' %(opts.app_label,  \
              opts.model_name),  args=[fk_id] )
            return format_html(
                 '<a target=_blank href="{}">{}</a>', related_url,tutor.username)
        else:
            return "No related object"
  username_link.short_description = "username"
  actions = [export_to_excel]

class StudentPreferSub(admin.StackedInline):
  def has_add_permission(self,request):
    return False
  can_delete = False
  model = StudentPreferSub
  fields = ('level','name')
  readonly_fields = ('level','name')

@admin.register(Student) 
class StudentAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
        return False
  list_display = ('full_name','gender','school','phone','wechat','whatsapp')
  list_filter = ('wait_match',)
  search_fields = ('full_name','username','email')
  fieldsets = (
    ('Personal information', {
      'fields': ('full_name','gender','school','grade','location',\
        'loc_nego','prefer_tutor_gender','signup_datetime','last_edit_time')
    }),
    ('Contact info',{
      'fields':('phone','wechat','whatsapp','email')
    })
  ) 
  readonly_fields = ('signup_datetime','last_edit_time')
  inlines = [IntentInStudentInline,]



@admin.register(StudentIntent)
class IntentAdmin(admin.ModelAdmin):
    readonly_fields = ['intent_tutor_link','student_link','final_tutor_link','last_edit_time']
    raw_id_fields = ['final_tutor',]
    list_display = ['student_name','last_edit_time','intent_level','intent_subject',\
      'final_tutor_name','successful_match','commission_collection_status',\
      'person_in_charge',]
    list_filter = ['successful_match','commission_collection_status','person_in_charge']
    search_fields = ['student_name','intent_subject','final_tutor_name','person_in_charge']
    radio_fields = {
      'overall_comment':admin.HORIZONTAL,
      'self_evaluation':admin.HORIZONTAL,
      'recommend_or_not':admin.HORIZONTAL
    }
    inlines = [OptionalTutorInline,FeedbackInline]
    def student_name(self,obj):
      return obj.student.full_name
    def final_tutor_name(self,obj):
      try:
        tname = obj.final_tutor.full_name
      except:
        tname = ''
      return tname
    fieldsets = (
      ["Student's intent",{
        'fields':('student_link','intent_level','intent_subject','intent_duration_per_lesson',\
          'intent_lesson_per_week','intent_start_time','intent_start_time_other',\
          'intent_remark1','intent_remark2','intent_remark3','intent_remark4',\
          'intent_remark5','intent_remark6','intent_weakness','last_edit_time'),
      }],
      ['Record states',{
        'fields':(('successful_match','commission_collection_status','failed','person_in_charge')),
      }],
      ['Contract and fees',{
        'classes':('collapse',),
        'fields':('final_tutor','final_tutor_link','startdate','chargedate','service_fees','freq','lesson_last','lesson_price'),
      }],
      ['Close call',{
        'classes': ('collapse',),
        'fields':('close_call_date','tuition_duration','overall_comment','q1','q2','self_evaluation',\
          'reasons','comment_charges','recommend_or_not'),
      }],
      ['',{
        'fields':('intent_tutor_link',)
      }]
    )

    def intent_tutor_link(self, instance):
        if instance:
            fk_id = instance.intent_tutor_id
        else:
            fk_id = None
        if fk_id:
            tutor = Tutor.objects.get(pk=fk_id)
            opts = tutor._meta
            related_url = reverse('admin:%s_%s_change' %(opts.app_label,  \
              opts.model_name),  args=[fk_id] )
            return format_html(
                 '<a target=_blank href="{}">{}</a>', related_url,tutor.full_name)
        else:
            return "The student didn't choose one."
    intent_tutor_link.short_description = "Intent tutor"
    def final_tutor_link(self, instance):
        if instance:
            fk_id = instance.final_tutor.id
        else:
            fk_id = None
        if fk_id:
            opts = instance._meta.get_field('final_tutor').rel.model._meta
            related_url = reverse('admin:%s_%s_change' %(opts.app_label,  \
              opts.model_name),  args=[fk_id] )
            return format_html(
                 '<a target=_blank href="{}">View the tutor</a>', related_url)
        else:
            return "No related object"
    final_tutor_link.short_description = "Check matched tutor"
    def student_link(self, instance):
        if instance:
            fk_id = instance.student.id
        else:
            fk_id = None
        if fk_id:
            student = instance.student
            opts = instance._meta.get_field('student').rel.model._meta
            related_url = reverse('admin:%s_%s_change' %(opts.app_label,  \
              opts.model_name),  args=[fk_id] )
            return format_html(
                 '<a target=_blank href="{}">{}</a>', related_url,student.full_name)
        else:
            return "No related object"
    student_link.short_description = "Check student"