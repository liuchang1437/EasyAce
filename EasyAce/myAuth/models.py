from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class Tutor(models.Model):
  class Meta:
    ordering = ['name']
  # 性别，Male和Female
  gender = models.CharField(u'gender',max_length=6)
  username = models.CharField(u"username",max_length=30)
  email = models.CharField(u'email address',max_length=40)
  # 电话
  phone = models.CharField(u'phone number',max_length=20)
  # state
  check = models.BooleanField(u'if checked?',default=False)
  top_teacher = models.BooleanField(u'if top tutors?',default=False)
  #photo
  photo = models.ImageField(u'photo',upload_to='photos')
  name = models.CharField(u'name',max_length=30)
  birth = models.CharField(u'birth day',max_length=12)
  school = models.CharField(u'school',max_length=50)
  wechat = models.CharField(max_length=30)
  whatsapp = models.CharField(max_length=30)
  # Middle School Graduation Test
  middle_test = models.CharField(u'middle test',max_length=50)
  middle_test_score = models.TextField(u'subjects and scores of middle test') # 格式为：sub1:score1;sub2:score2...
  # High School Graduation Test
  high_test = models.CharField(u'high test',max_length=50)
  high_test_score = models.TextField(u'subjects and scores of high test') # 格式为：sub1:score1;sub2:score2...
  # Preference of Teaching Subjects
  prefer_teach = models.TextField(u'subjects prefered to teach',) # 格式为：lev1:sub1;level2:sub2...
  regions = models.CharField(max_length=30) # 格式为：Preference1;preference2;preference3
  region1 = models.CharField(max_length=30,default='none')
  region2 = models.CharField(max_length=30,default='none')
  region3 = models.CharField(max_length=30,default='none')
  middle_sub_other = models.TextField(u'subjects and scores of middle test(other)',null=True,blank=True) # other,sub1,score1;other,sub2,score2;...
  high_sub_other = models.TextField(u'subjects and scores of high test(other)',null=True,blank=True) # other,sub1,score1;other,sub2,score2;...
  teaching_sub_other = models.TextField(u'subjects prefered to teach(other)',null=True,blank=True) # level1,other,sub1;lev2,other,sub2...

  duration = models.CharField(max_length=12)
  num_taught = models.CharField(u'numbers of students taught',max_length=10)
  achievement = models.TextField()
  base_info = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  def get_single(self,field_name):
    results = getattr(self,field_name).split(';')
    try:
      results.remove('')
    finally:
      return results
  def get_prefer_teach(self):
    result = []
    pairs = self.prefer_teach.split(';')
    for pair in pairs:
      if pair.strip()=='':
        continue
      result.append(pair.split(':'))
    return result

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
  def __str__(self):
    return self.name
class Student(models.Model):
  class Meta:
    ordering = ['name']
  # 性别，Male和Female
  gender = models.CharField(max_length=6)
  username = models.CharField(max_length=30)
  email = models.CharField('email address',max_length=40)
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
  loc_nego = models.CharField('If tuition location negotiable',max_length=20)
  exam_type = models.CharField('exam type',max_length=50)
  # 想要上的课程
  subjects = models.TextField() # 格式为 sub1;sub2;sub3...
  duration_per_lesson = models.CharField('time per lesson',max_length=12)
  start_time = models.CharField('start time',max_length=8)
  lesson_per_week = models.CharField('lesson per week',max_length=12)
  prefer_tutor = models.CharField('preference about tutor',max_length=7)
  start_time_other = models.CharField('start time(other)',max_length=12,null=True,blank=True)
  #num_taught = models.CharField(max_length=10)
  remarks = models.TextField('remarks') # 格式为 1;2;3;...
  subjects_other = models.TextField('subjects(other)',null=True,blank=True) # 格式韦 sub1;sub2;sub3;...
  weakness = models.TextField()
  #achievement = models.CharField(max_length=300)

  wait_match = models.BooleanField(u'等待分配教师',default=True)
  prefer_tutors = models.ManyToManyField(Tutor,null=True,blank=True)
  base_info = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  def get_single(self,field_name):
    results = getattr(self,field_name).split(';')
    try:
      results.remove('')
    finally:
      return results
  def __str__(self):
    return self.name


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

class Record(models.Model):
  if_confirmed = models.BooleanField(default=False,verbose_name=u'双方是否确认')
  startdate = models.DateField(u'确认日期',blank=True,null=True)
  chargedate = models.DateField(u'收费日期',blank=True,null=True)
  service_fees = models.CharField(u'中介费用',blank=True,null=True,max_length=20)
  freq = models.CharField(u'每周课时数',blank=True,null=True,max_length=30)
  lesson_last = models.CharField(u'每节课时长',blank=True,null=True,max_length=30)
  lesson_price = models.CharField(u'每节课费用',blank=True,null=True,max_length=30)
  admin_name = models.CharField(u'管理员姓名',max_length=30)

  tutor = models.ForeignKey(Tutor,on_delete=models.CASCADE,related_name='records',limit_choices_to={'check':True})
  student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='records')
  # def get_tutor_name(self):
  #   return self.tutor.name
  # def get_student_name(self):
  #   return self.student.name

  # tutor_name = models.CharField(max_length=20,default=get_tutor_name)
  # student_name = models.CharField(max_length=20,default=get_student_name)

  def __str__(self):
    return 'student:{},tutor:{},firmed:{}'.format(self.student,self.tutor,self.if_confirmed)

class Feedback(models.Model):
  tutor = models.ForeignKey(Tutor,on_delete=models.CASCADE,related_name='feedbacks',limit_choices_to={'check':True})
  student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='Feedbacks')
  date = models.DateField()
  remark = models.TextField(u'学生对教师评价',blank=True)