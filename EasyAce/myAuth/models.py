from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class Tutor(models.Model):
  # 性别，Male和Female
  gender = models.CharField(max_length=6)
  # 电话
  phone = models.CharField(max_length=20)
  name = models.CharField(max_length=30)
  birth = models.DateField()
  school = models.CharField(max_length=50)
  wechat = models.CharField(max_length=30)
  whatsapp = models.CharField(max_length=30)
  # Middle School Graduation Test
  # High School Graduation Test
  regions = models.CharField(max_length=30) # 格式为：Preference1,preference2,preference3
  duration = models.CharField(max_length=12)
  num_st_taught = models.CharField(max_length=10)
  achievement = models.CharField(max_length=300)
  base_info = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
class Student(models.Model):
  extra_info = models.TextField()
  base_info = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
class MyUser(AbstractUser):
  # built-in 数据域有：username,first_name,last_name,email,password
  # 额外添加的基本数据域如下：
  # 用户类型，分为Tutor和Student
  role = models.CharField(max_length=6)

  # 根据用户类型返回用户的额外信息。
  def get_user(self):
    if self.role == 'Tutor':
      if self.tutor:
        return self.tutor 
    else:
      if self.student:
        return self.student