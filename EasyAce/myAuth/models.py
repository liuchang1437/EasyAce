from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class Tutor(models.Model):
  # extra_info 用于测试
  extra_info = models.TextField()
  base_info = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
class Student(models.Model):
  extra_info = models.TextField()
  base_info = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
class MyUser(AbstractUser):
  # built-in 数据域有：username,first_name,last_name,email,password
  # 额外添加的基本数据域如下：
  # 用户类型，分为Tutor和Student
  TUTOR = 'TU'
  STUDENT = 'ST'
  ROLE_CHOICES = (
    (TUTOR,'Tutor'),
    (STUDENT,'Student'),
  )
  role = models.CharField(max_length=2,choices=ROLE_CHOICES,blank=False)
  # 性别，Male和Female
  MALE = 'M'
  FEMALE = 'F'
  GENDER_CHOICES = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
  )
  gender = models.CharField(max_length=2,choices=GENDER_CHOICES,blank=False)
  # 电话
  phone = models.CharField(max_length=20)

  # 根据用户类型返回用户的额外信息。
  def get_user(self):
    if self.role == self.TUTOR:
      if self.tutor:
        return self.tutor 
    else:
      if self.student:
        return self.student