from django.contrib import admin
from .models import Tutor,Student,MyUser,Record,Feedback,\
  StudentPreferSub,PreferSubject,ReferSubject
# Register your models here.

class RecordInline(admin.StackedInline):
  colapse = True
  model = Record
  extra = 0
  raw_id_fields = ('tutor',)
class FeedbackInline(admin.StackedInline):
  model = Feedback
  extra = 0
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
  list_filter = ('check','top_teacher')
  search_fields = ('name','username','email')
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
  def cal_star_rating(self,request,queryset):
    for obj in queryset:
      obj.cal_sr()
      obj.save()
    self.message_user(request,'Successfully updated star-ratings of the selected tutors!')
  cal_star_rating.short_description = 'Update the star rating'
  actions = [cal_star_rating]

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

  