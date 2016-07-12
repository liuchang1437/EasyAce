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
  list_filter = ('check','region1','region2','region3')


@admin.register(Student) 
class StudentAdmin(admin.ModelAdmin):
  list_display = (username,'name',email,'wait_match')
  list_filter = ('wait_match',)

@admin.register(Record) 
class RecordAdmin(admin.ModelAdmin):
  pass


@admin.register(Feedback) 
class FeedbackAdmin(admin.ModelAdmin):
  pass
  