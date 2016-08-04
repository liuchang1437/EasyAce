from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Tutor(models.Model):
  class Meta:
    ordering = ['username','sr']
  ############### Information Fields Start ###############
  username = models.CharField(u"username",max_length=30) # username and email, 应该和MyUser中的一致
  name = models.CharField(u'name',max_length=50)
  gender = models.CharField(u'gender',max_length=6) # 性别，Male和Female
  birth = models.CharField(u'birthday',max_length=12)
  email = models.CharField(u'email address',max_length=40)
  phone = models.CharField(u'phone number',max_length=20) # 电话
  school = models.CharField(u'school',max_length=50)
  wechat = models.CharField(max_length=30,null=True,blank=True)
  whatsapp = models.CharField(max_length=30,null=True,blank=True)
  photo = models.ImageField(u'photo',upload_to='photos')
  base_info = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  ############### Information Fields End ###############

  ############### State Fields Start ###############
  check = models.BooleanField(u'if checked?',default=False)
  top_teacher = models.BooleanField(u'if top tutors?',default=False)
  ############### State Fields End ###############
  
  ############### Profile Fields Start ###############
  tutor_location1 = models.CharField(max_length=30,default='not chosen',blank=True)
  tutor_location2 = models.CharField(max_length=30,default='not chosen',blank=True)
  tutor_location3 = models.CharField(max_length=30,default='not chosen',blank=True)
  teach_duration = models.CharField(max_length=12)
  num_taught = models.CharField(u'教过的学生数',max_length=10)
  achievement = models.TextField()
  ############### Profile Fields End ###############

  ############### Star Rating Start ###############
  isr = models.FloatField(default=0)
  sr = models.FloatField(u'Star rating',default=0)
  interview_result = models.FloatField(default=0)
  def cal_isr(self):
    isr = 0
    times_total = 0
    for sub in self.refer_subs.all():
      # 空的课程，就跳过
      if not sub.level:
        continue
      # 多于4个，则不计入isr
      if sub.rank==5:
        break
      local = 0
      # 根据不同的考试类型，以及不同的成绩，计算分数
      if sub.level=='O-LEVEL':
        if sub.score=='A1':
          local = 4
        elif sub.score=='A2':
          local = 2
      if sub.level=='IB (Middle Years Programme)':
        if sub.score=='7':
          local = 4
        elif sub.score=='6':
          local = 2
      if sub.level=='Zhongkao':
        if sub.score=='>135':
          local = 4
        elif sub.score=='125-135':
          local = 2
      if sub.level=='A-LEVEL':
        if sub.score=='A':
          local = 4
        elif sub.score=='B':
          local = 2
      if sub.level=='IB (Diploma Programme)':
        if sub.score=='7':
          local = 4
        elif sub.score=='6':
          local = 2
      if sub.level=='Gaokao':
        if sub.score=='>135':
          local = 4
        elif sub.score=='125-135':
          local = 2
      # 心仪的科目顺序不同，也会造成isr的不同
      if sub.rank==1:
        times = 0.4
      if sub.rank==2:
        times = 0.3
      if sub.rank==3:
        times = 0.2
      if sub.rank==4:
        times = 0.1
      times_total += times
      isr += local*times
    if times_total:
      isr = isr*10/times_total
    if self.teach_duration == '1 month':
      isr += 1
    if self.teach_duration == '1-3 months':
      isr += 3
    if self.teach_duration == '3-6 months':
      isr += 5
    if self.teach_duration == '6-12 months':
      isr += 7
    if self.teach_duration == '>1 year':
      isr += 9
    if self.teach_duration == '>2 years':
      isr += 10
    if self.num_taught == '1-3':
      isr += 2
    if self.num_taught == '4-6':
      isr += 6
    if self.num_taught == '7-9':
      isr += 8
    if self.num_taught == '>=10':
      isr += 10
    self.isr = isr
  def cal_sr(self):
    self.cal_isr()
    isr = self.isr + self.interview_result
    fsr = 0
    fsr_time = 0
    for feedback in self.feedbacks.all():
      local_fsr = 0
      # attitude
      if feedback.attitude == 'Excellent':
        local_fsr += 20
      if feedback.attitude == 'Good':
        local_fsr += 10
      if feedback.attitude == 'Poor':
        local_fsr -= 10
      if feedback.attitude == 'Very Poor':
        local_fsr -= 20
      # preparation
      if feedback.preparation == 'Excellent':
        local_fsr += 20
      if feedback.preparation == 'Good':
        local_fsr += 10
      if feedback.preparation == 'Poor':
        local_fsr -= 10
      if feedback.preparation == 'Very Poor':
        local_fsr -= 20
      # clarity
      if feedback.clarity == 'Excellent':
        local_fsr += 20
      if feedback.clarity == 'Good':
        local_fsr += 10
      if feedback.clarity == 'Poor':
        local_fsr -= 10
      if feedback.clarity == 'Very Poor':
        local_fsr -= 20
      # knowledgeability
      if feedback.knowledgeability == 'Excellent':
        local_fsr += 20
      if feedback.knowledgeability == 'Good':
        local_fsr += 10
      if feedback.knowledgeability == 'Poor':
        local_fsr -= 10
      if feedback.knowledgeability == 'Very Poor':
        local_fsr -= 20
      # outcome
      if feedback.outcome == 'Excellent':
        local_fsr += 20
      if feedback.outcome == 'Good':
        local_fsr += 10
      if feedback.outcome == 'Poor':
        local_fsr -= 10
      if feedback.outcome == 'Very Poor':
        local_fsr -= 20
      if feedback.attend == 'On time':
        local_fsr += 10
      if feedback.attend == '5-15 min':
        local_fsr -= 5
      if feedback.attend == '15-30 min':
        local_fsr -= 10
      if feedback.attend == '>30 min':
        local_fsr -= 20
      fsr += local_fsr*feedback.time
      fsr_time += feedback.time
    sr = (30*isr + fsr)/(30 + fsr_time)
    self.sr = round(sr,2)
    
  ############### Star Rating End ###############
  def __str__(self):
    return self.name
class PreferSubject(models.Model):
  level = models.CharField(max_length=30)
  name = models.CharField(max_length=30)
  rank = models.IntegerField(editable=False)
  other = models.BooleanField(default=False)
  tutor = models.ForeignKey(Tutor,related_name='prefer_subs',related_query_name='prefer_sub')
  def __str__(self):
    return 'rank {}'.format(self.rank)
class ReferSubject(models.Model):
  level = models.CharField(max_length=30)
  name = models.CharField(max_length=30)
  score = models.CharField(max_length=20,default='0')
  rank = models.IntegerField(editable=False)
  other = models.BooleanField(default=False)
  tutor = models.ForeignKey(Tutor,related_name='refer_subs',related_query_name='refer_sub')
  def __str__(self):
    return 'rank {}'.format(self.rank)

class Student(models.Model):
  class Meta:
    ordering = ['username']
  ############### Base Info Start ###############
  username = models.CharField(u"username",max_length=30)
  name = models.CharField(max_length=30)
  gender = models.CharField(max_length=6)
  email = models.CharField('email address',max_length=40)
  phone = models.CharField(max_length=20)
  school = models.CharField(max_length=50)
  grade = models.CharField(max_length=20)
  wechat = models.CharField(max_length=30)
  whatsapp = models.CharField(max_length=30)
  base_info = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  ############### Base Info End ###############

  ############### Preference Start ###############
  location = models.CharField(max_length=100)
  loc_nego = models.CharField('If tuition location negotiable',max_length=20)
  time_per_lesson = models.CharField('time per lesson',max_length=12)
  lesson_per_week = models.CharField('lesson per week',max_length=12)
  start_time = models.CharField('start time',max_length=8)
  start_time_other = models.CharField('start time(other)',max_length=12,null=True,blank=True)
  prefer_tutor_gender = models.CharField('preference about tutor',max_length=7)
  remarks = models.TextField('remarks',blank=True,null=True) # 格式为 1;2;3;...
  weakness = models.TextField(blank=True,null=True)
  ############### Preference End ###############

  ############### State Start ###############
  wait_match = models.BooleanField(u'等待分配教师',default=True)
  tutors_chosen = models.ManyToManyField(Tutor)
  ############### State End ###############
  
  def get_remarks(self):
    results = self.remarks.split(';')
    try:
      results.remove('')
    finally:
      return results
  def __str__(self):
    return self.name
class StudentPreferSub(models.Model):
  level = models.CharField(max_length=30)
  name = models.CharField(max_length=30)
  rank = models.IntegerField(editable=False)
  other = models.BooleanField(default=False)
  student = models.ForeignKey(Student,related_name='prefer_subs',related_query_name='prefer_sub')
  def __str__(self):
    return 'rank {}'.format(self.rank)


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
  tutor = models.ForeignKey(Tutor,on_delete=models.CASCADE,related_name='records',limit_choices_to={'check':True})
  student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='records')
  if_confirmed = models.BooleanField(default=False,verbose_name=u"Tutor's Consent'")
  startdate = models.DateField(u'Contract Signing Date',default=timezone.now,blank=True)
  chargedate = models.DateField(u'Commission Due Date',blank=True,null=True)
  service_fees = models.CharField(u'Total Commission Fee',blank=True,null=True,max_length=20)
  freq = models.CharField(u'Actual no. of lessons per week',blank=True,null=True,max_length=30)
  lesson_last = models.CharField(u'Actual no. of hours per lesson:(hours)',blank=True,null=True,max_length=30)
  lesson_price = models.CharField(u'Hourly Fee',blank=True,null=True,max_length=30)
  admin_name = models.CharField(u'Person-in-charge',max_length=30)

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
  student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='feedbacks')
  subject = models.CharField(max_length=50)
  attend = models.CharField(max_length=20)
  ## if ontime = Yes, attend = On time, else attend = late_time
  ## 
  # 5 aspects of evaluation:
  attitude = models.CharField(max_length=10)
  preparation = models.CharField(max_length=10)
  clarity = models.CharField(max_length=10)
  knowledgeability = models.CharField(max_length=10)
  outcome = models.CharField(max_length=10)
  # evaluation end
  
  time = models.FloatField(u'授课时间（小时）') # tuition_hour
  date = models.DateField(default=timezone.now)
  comment = models.TextField(u'学生对教师评价',blank=True)