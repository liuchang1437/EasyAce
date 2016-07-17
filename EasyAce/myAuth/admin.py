from django.contrib import admin
from .models import Tutor,Student,MyUser,Record,Feedback
# Register your models here.

def email(obj):
  return obj.base_info.email
def username(obj):
  return obj.base_info.username
def records(obj):
    return obj.records.all()

@admin.register(Tutor) 
class TutorAdmin(admin.ModelAdmin):
  list_display = (username,'name',email,'check')
  list_filter = ('check','top_teacher')
  
  fieldsets = (
    ('Base info', {
      'fields': ('name','username','gender','birth','school','middle_test','middle_test_score',\
        'middle_sub_other','high_test','high_test_score','high_sub_other',\
        'prefer_teach','teaching_sub_other','region1',\
        'region2','region3','duration','num_taught','achievement')
    }),
    ('Contact info',{
      'fields':('phone','wechat','whatsapp','email')
    }),
    ('Options',{
      'fields':('check','top_teacher')
    })
  ) 

@admin.register(Student) 
class StudentAdmin(admin.ModelAdmin):
  list_display = (username,'name',email,'wait_match')
  list_filter = ('wait_match',)
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

def student(obj):
  return obj.tutor.name
def tutor(obj):
  return obj.student.name

@admin.register(Record) 
class RecordAdmin(admin.ModelAdmin):
  list_display = (student,tutor,'if_confirmed')
  list_filter = ('if_confirmed',)
  fieldsets = (
    ('Required', {
      'fields': ('admin_name','student','tutor')
    }),
    ('Others',{
      'fields':('startdate','chargedate','service_fees','freq','lesson_last',\
        'lesson_price')
    }),
    ('Options',{
      'fields':('if_confirmed',)
    })
  ) 

@admin.register(Feedback) 
class FeedbackAdmin(admin.ModelAdmin):
  list_display = (student,tutor,'date')
  