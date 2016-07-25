from django.contrib import admin
from django.http import HttpResponse
from .models import Tutor,Student,MyUser,Record,Feedback,\
  StudentPreferSub,PreferSubject,ReferSubject
import xlwt
# Register your models here.

class RecordInline(admin.StackedInline):
  colapse = True
  model = Record
  extra = 0
  raw_id_fields = ('tutor',)
class FeedbackInline(admin.StackedInline):
  model = Feedback
  extra = 0
  raw_id_fields = ('student',)
class PreferSub(admin.StackedInline):
  def has_add_permission(self,request):
    return False
  can_delete = False
  model = PreferSubject
  fields = ('level','name')
  readonly_fields = ('level','name')
class ReferSub(admin.StackedInline):
  def has_add_permission(self,request):
    return False
  can_delete = False
  model = ReferSubject
  fields = ('level','name','score')
  readonly_fields = ('level','name','score')

@admin.register(Tutor) 
class TutorAdmin(admin.ModelAdmin):
  list_display = ('username','name','email','check','sr')
  list_filter = ('check','top_teacher','prefer_sub__level','prefer_sub__name')
  search_fields = ('name','username','email','prefer_sub__level','prefer_sub__name')
  fieldsets = (
    ('Base information', {
      'fields': ('name','username','gender','birth','school',\
        'tutor_location1',\
        'tutor_location2','tutor_location3','teach_duration',\
        'num_taught','achievement','sr')
    }),
    ('Contact information',{
      'fields':('phone','wechat','whatsapp','email')
    }),
    ('Options',{
      'fields':('check','top_teacher','interview_result')
    })
  ) 
  readonly_fields = ('name','username','gender','birth','school',\
    'tutor_location1','tutor_location2','tutor_location3',\
    'teach_duration','num_taught','achievement','phone',\
    'wechat','whatsapp','email','sr')
  inlines = [PreferSub,ReferSub,FeedbackInline]
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
    sheet.write(0,0,'name')
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
      sheet.write(row,0,tutor.name)
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

  actions = [cal_star_rating,export_to_excel]

class StudentPreferSub(admin.StackedInline):
  def has_add_permission(self,request):
    return False
  can_delete = False
  model = StudentPreferSub
  fields = ('level','name')
  readonly_fields = ('level','name')

@admin.register(Student) 
class StudentAdmin(admin.ModelAdmin):
  list_display = ('username','name','email','wait_match')
  list_filter = ('wait_match',)
  search_fields = ('name','username','email')
  fieldsets = (
    ('Base information', {
      'fields': ('name','username','gender','school','grade','location',\
        'loc_nego',\
        'start_time','start_time_other','time_per_lesson',\
        'lesson_per_week','prefer_tutor_gender','remarks','weakness','tutors_chosen')
    }),
    ('Contact info',{
      'fields':('phone','wechat','whatsapp','email')
    }),
    ('Options',{
      'fields':('wait_match',)
    })
  ) 
  readonly_fields = ('name','username','gender','grade','school',\
    'location','loc_nego','start_time',\
    'start_time_other','time_per_lesson','lesson_per_week','remarks',\
    'wechat','whatsapp','email','prefer_tutor_gender','weakness','tutors_chosen','phone')
  inlines = [StudentPreferSub,RecordInline]

  