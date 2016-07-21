from django.contrib import admin
from .models import Tutor,Student,MyUser,Record,Feedback,PreferSubject,ReferSubject
# Register your models here.

def email(obj):
  return obj.base_info.email
def username(obj):
  return obj.base_info.username
def records(obj):
    return obj.records.all()


class RecordInline(admin.StackedInline):
  colapse = True
  model = Record
  extra = 0
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
  list_display = ('username','name','email','check')
  list_filter = ('check','top_teacher')
  search_fields = ('name','username','email')
  fieldsets = (
    ('Base information', {
      'fields': ('name','username','gender','birth','school',\
        'tutor_location1',\
        'tutor_location2','tutor_location3','teach_duration',\
        'num_taught','achievement')
    }),
    ('Contact information',{
      'fields':('phone','wechat','whatsapp','email')
    }),
    ('Options',{
      'fields':('check','top_teacher')
    })
  ) 
  readonly_fields = ('name','username','gender','birth','school',\
    'tutor_location1','tutor_location2','tutor_location3',\
    'teach_duration','num_taught','achievement','phone',\
    'wechat','whatsapp','email')
  inlines = [PreferSub,ReferSub,FeedbackInline]
@admin.register(Student) 
class StudentAdmin(admin.ModelAdmin):
  list_display = (username,'name',email,'wait_match')
  list_filter = ('wait_match',)
  search_fields = ('name','username')
  
  fieldsets = (
    ('Base info', {
      'fields': ('name','username','gender','school','grade','location',\
        'loc_nego','exam_type','subjects','subjects_other',\
        'start_time','start_time_other','duration_per_lesson',\
        'lesson_per_week','prefer_tutor','prefer_tutors','remarks','weakness')
    }),
    ('Contact info',{
      'fields':('phone','wechat','whatsapp','email')
    }),
    ('Options',{
      'fields':('wait_match',)
    })
  ) 
  inlines = [RecordInline]

  