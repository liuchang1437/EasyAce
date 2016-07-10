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
  birth = models.CharField(max_length=12)
  school = models.CharField(max_length=50)
  wechat = models.CharField(max_length=30)
  whatsapp = models.CharField(max_length=30)
  # Middle School Graduation Test
  middle_test = models.CharField(max_length=50)
  middle_test_score = models.TextField() # 格式为：sub1:score1;sub2:score2...
  # High School Graduation Test
  high_test = models.CharField(max_length=50)
  high_test_score = models.TextField() # 格式为：sub1:score1;sub2:score2...
  # Preference of Teaching Subjects
  prefer_teach = models.TextField() # 格式为：lev1:sub1;level2:sub2...
  regions = models.CharField(max_length=30) # 格式为：Preference1;preference2;preference3
  middle_sub_other = models.TextField() # other,sub1,score1;other,sub2,score2;...
  high_sub_other = models.TextField() # other,sub1,score1;other,sub2,score2;...
  teaching_sub_other = models.TextField() # level1,other,sub1;lev2,other,sub2...

  duration = models.CharField(max_length=12)
  num_taught = models.CharField(max_length=10)
  achievement = models.CharField(max_length=300)
  base_info = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  def get_single(self,field_name):
    results = getattr(self,field_name).split(';')
    try:
      results.remove('')
    finally:
      return results
  def get_pairs(self,field_name):
    pairs = getattr(self,field_name).split(';')
    result = {}
    for pair in pairs:
      if pair.strip()=='':
        continue
      index = pair.find(':')
      first = pair[:index]
      second = pair[index+1:]
      result[first] = second
    return result
  def get_triple(self,field_name):
    triples = getattr(self,field_name).split(';')
    result = []
    for triple in triples:
      if triple.strip()=='':
        continue
      result.append(triple.split(','))
    return result
  # def return_middle_test(self):
  #   pairs = self.middle_test_score.split(';')
  #   result = {}
  #   for pair in pairs:
  #     if pair.strip()=='':
  #       continue
  #     index = pair.find(':')
  #     sub = pair[:index]
  #     score = pair[index+1:]
  #     result[sub] = score
  #   return result
  # def return_prefer_teach(self):
  #   pairs = self.prefer_teach.split(';')
  #   result = {}
  #   for pair in pairs:
  #     if pair.strip()=='':
  #       continue
  #     index = pair.find(':')
  #     sub = pair[:index]
  #     score = pair[index+1:]
  #     result[sub] = score
  #   return result
  # def return_high_test(self):
  #   pairs = self.high_test_score.split(';')
  #   result = {}
  #   for pair in pairs:
  #     if pair.strip()=='':
  #       continue
  #     index = pair.find(':')
  #     sub = pair[:index]
  #     score = pair[index+1:]
  #     result[sub] = score
  #   return result
class Student(models.Model):
  # 性别，Male和Female
  gender = models.CharField(max_length=6)
  # 电话
  phone = models.CharField(max_length=20)
  # 姓名
  name = models.CharField(max_length=30)
  # 生日
  #birth = models.DateField()
  school = models.CharField(max_length=50)
  wechat = models.CharField(max_length=30)
  whatsapp = models.CharField(max_length=30)
  grade = models.CharField(max_length=20)
  location = models.CharField(max_length=100)
  loc_nego = models.CharField(max_length=20)
  exam_type = models.CharField(max_length=50)
  # 想要上的课程
  subjects = models.TextField() # 格式为 sub1;sub2;sub3...
  duration_per_lesson = models.CharField(max_length=12)
  start_time = models.CharField(max_length=8)
  lesson_per_week = models.CharField(max_length=12)
  prefer_tutor = models.CharField(max_length=7)
  start_time_other = models.CharField(null=True,max_length=12)
  #num_taught = models.CharField(max_length=10)
  remarks = models.TextField() # 格式为 1;2;3;...
  subjects_other = models.TextField() # 格式韦 sub1;sub2;sub3;...
  weakness = models.TextField()
  #achievement = models.CharField(max_length=300)
  base_info = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  def get_single(self,field_name):
    results = getattr(self,field_name).split(';')
    try:
      results.remove('')
    finally:
      return results


class MyUser(AbstractUser):
  # built-in 数据域有：username,first_name,last_name,email,password
  # 额外添加的基本数据域如下：
  # 用户类型，分为tutor和student
  role = models.CharField(max_length=7)

  # 根据用户类型返回用户的额外信息。
  def get_user(self):
    if self.role == 'tutor':
      try:
        return self.tutor
      except:
        return False
    elif self.role == 'student':
      try:
        return self.student
      except:
        return False
    else:
      return False