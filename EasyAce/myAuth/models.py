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
  #name = models.CharField(u'name',max_length=50)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  full_name = models.CharField(u"name",max_length=100)
  gender = models.CharField(u'gender',max_length=6) # 性别，Male和Female
  birth = models.CharField(u'birthday',max_length=12)
  email = models.CharField(u'email address',max_length=40)
  phone = models.CharField(u'phone number',max_length=20) # 电话
  school = models.CharField(u'school',max_length=50)
  wechat = models.CharField(max_length=30,null=True,blank=True)
  whatsapp = models.CharField(max_length=30,null=True,blank=True)
  photo = models.ImageField(u'photo',upload_to='photos',default='default_photo.jpg')
  base_info = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  signup_datetime = models.DateTimeField(u'Signup date',auto_now_add=True,editable=True)
  last_edit_time = models.DateTimeField(u'Last modified ',auto_now=True,editable=True)
  # signup_datetime.editable=True
  # last_edit_time.editable=True
  ############### Information Fields End ###############

  ############### State Fields Start ###############
  check = models.BooleanField(u'if checked?',default=False)
  top_teacher = models.BooleanField(u'if top tutors?',default=False)
  ############### State Fields End ###############
  
  ############### Profile Fields Start ###############
  tutor_location1 = models.CharField(max_length=30,default='not chosen')
  tutor_location2 = models.CharField(max_length=30,default='not chosen',blank=True,null=True)
  tutor_location3 = models.CharField(max_length=30,default='not chosen',blank=True,null=True)
  teach_duration = models.CharField(u'experience',max_length=12)
  num_taught = models.CharField(u'Amount of students have taught',max_length=10)
  achievement = models.TextField(blank=True,null=True)
  ############### Profile Fields End ###############

  ############### Star Rating Start ###############
  isr = models.FloatField(default=0)
  sr = models.FloatField(u'Star rating',default=0)
  interview_result = models.FloatField(default=0)
  ############### Star Rating  End #################
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
  def save(self, *args, **kwargs):
      super(Tutor, self).save(*args, **kwargs) # Call the "real" save() method.
      self.cal_sr()
      super(Tutor, self).save(*args, **kwargs)
  ############### Star Rating End ###############
  def __str__(self):
    return self.full_name
class Interview(models.Model):
  INTERVIEW_CHOICES = (
    ('0','0'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
  )
  interview_presentability = models.CharField(u'Presentability',max_length=2,choices=INTERVIEW_CHOICES,default=0)
  interview_friendliness = models.CharField(u'Firendliness and care',max_length=2,choices=INTERVIEW_CHOICES,default=0)
  interview_crisis_hand = models.CharField(u'Crisis handling ability',max_length=2,choices=INTERVIEW_CHOICES,default=0)
  interview_communication = models.CharField(u'Communication Skill',max_length=2,choices=INTERVIEW_CHOICES,default=0)

  interview_grade = models.CharField(u'Year of Study',max_length=100,blank=True,null=True)
  interview_major = models.CharField(u'Major',max_length=100,blank=True,null=True)
  interview_num_taught = models.CharField(u'No. of Students Taught',max_length=100,blank=True,null=True)
  interview_effect = models.TextField(u'Outcome',blank=True,null=True)
  interview_fees = models.CharField(u'Fee Charged',max_length=100,blank=True,null=True)
  interview_how_to_range_course = models.TextField(u'How do you arrange a two-hour class?',blank=True,null=True)
  interview_tutor_type = models.CharField(u'Character/Type',max_length=100,blank=True,null=True)
  interview_why_you_good = models.TextField(u'Why are you a good tutor?',blank=True,null=True)
  interview_how_relation_with_stu = models.TextField(u'How do you manage your relationship with students?',blank=True,null=True)
  interview_how_rel_with_prntofstu = models.TextField(u'How do you manage your relationship with parents?',blank=True,null=True)
  interview_how_long = models.CharField(u'How long do you plan to teach?',max_length=100,blank=True,null=True)
  interview_why_tutor = models.TextField(u'Why do you want to become a tutor? (Motive)',blank=True,null=True)
  interview_what_matter = models.TextField(u'What kind of students would you like or not like to teach? Prioritize the criteria',blank=True,null=True)
  interview_other_sub = models.TextField(u'Can you teach some other subjects with tutor shortage? (Give a few choices based on the situation; remind the interviewee about potential higher earnings)',blank=True,null=True)
  interview_can_teach_tutor = models.TextField(u'Do you know tutors who can teach the above-mentioned subjects?',blank=True,null=True)
  interview_recommend = models.TextField(u'Can you provide trainings for unexperienced tutors?',blank=True,null=True)
  interview_new_tutor_training = models.TextField(u'Do you need newbie training? ',blank=True,null=True)
  interview_comment = models.TextField(u'Comments by Interviewer',blank=True,null=True)
  interview_remark = models.TextField(u'Others',blank=True,null=True)
  tutor = models.OneToOneField(Tutor, on_delete=models.CASCADE)
  def cal_inter_result(self):
    r = 0
    r += int(self.interview_presentability)
    r += int(self.interview_friendliness)
    r += int(self.interview_crisis_hand)
    r += int(self.interview_communication)
    self.tutor.interview_result = r
  def save(self, *args, **kwargs):
      super(Interview, self).save(*args, **kwargs) # Call the "real" save() method.
      self.cal_inter_result()
      self.tutor.save()
class PreferSubject(models.Model):
  level = models.CharField(max_length=30,default='Not chosen')
  name = models.CharField(u'subject',max_length=30,default='Not chosen')
  rank = models.IntegerField(editable=False)
  other = models.BooleanField(default=False)
  tutor = models.ForeignKey(Tutor,related_name='prefer_subs',related_query_name='prefer_sub')
  def __str__(self):
    return '{}'.format(self.rank)
class ReferSubject(models.Model):
  level = models.CharField(max_length=30,default='Not chosen')
  name = models.CharField(u'subject',max_length=30,default='Not chosen')
  score = models.CharField(max_length=20,default='0')
  rank = models.IntegerField(editable=False)
  other = models.BooleanField(default=False)
  tutor = models.ForeignKey(Tutor,related_name='refer_subs',related_query_name='refer_sub')
  def __str__(self):
    return '{}'.format(self.rank)

class Student(models.Model):
  class Meta:
    ordering = ['username']
  ############### Base Info Start ###############
  username = models.CharField(u"username",max_length=30)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  full_name = models.CharField(u"name",max_length=100)
  #name = models.CharField(max_length=30)
  gender = models.CharField(max_length=6)
  email = models.CharField('email address',max_length=40)
  phone = models.CharField(max_length=20)
  school = models.CharField(max_length=50)
  grade = models.CharField(max_length=20)
  wechat = models.CharField(max_length=30,blank=True,null=True)
  whatsapp = models.CharField(max_length=30,blank=True,null=True)
  base_info = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  signup_datetime = models.DateTimeField(u'Signup date',auto_now_add=True,editable=True)
  last_edit_time = models.DateTimeField(u'Last modified',auto_now=True,editable=True)
  # signup_datetime.editable=True
  # last_edit_time.editable=True
  ############### Base Info End ###############

  ############### Preference Start ###############
  location = models.CharField(max_length=100)
  loc_nego = models.CharField('If tuition location negotiable',max_length=20)
  prefer_tutor_gender = models.CharField('preference about tutor',max_length=7)
  ############### Preference End ###############

  ############### State Start ###############
  wait_match = models.BooleanField(u'等待分配教师',default=True)
  tutors_chosen = models.ManyToManyField(Tutor)
  ############### State End ###############

  #admin_name = models.CharField(u'Person-in-charge',max_length=30,blank=True,null=True)
  intent_cnt = models.IntegerField(default=0)
  
  def __str__(self):
    return self.full_name

class StudentIntent(models.Model):
  ############# Intent base information ############
  intent_level = models.CharField(max_length=30)
  intent_subject = models.CharField(max_length=30)
  intent_subject_other = models.BooleanField(default=False)
  intent_duration_per_lesson = models.CharField('time per lesson',max_length=12)
  intent_lesson_per_week = models.CharField('lesson per week',max_length=12)
  intent_start_time = models.CharField('start time',max_length=8)
  intent_start_time_other = models.DateField('start time(other)',null=True,blank=True)
  intent_remark1 = models.CharField(max_length=100,blank=True,null=True)
  intent_remark2 = models.CharField(max_length=100,blank=True,null=True)
  intent_remark3 = models.CharField(max_length=100,blank=True,null=True)
  intent_remark4 = models.CharField(max_length=100,blank=True,null=True)
  intent_remark5 = models.CharField(max_length=100,blank=True,null=True)
  intent_remark6 = models.CharField(max_length=200,blank=True,null=True)
  intent_weakness = models.TextField(blank=True,null=True)
  rank = models.IntegerField(blank=True,null=True)

  ############# Related tutor and studnet  ############
  intent_tutor_id = models.IntegerField(blank=True,null=True)
  student = models.ForeignKey(Student,related_name='intents',related_query_name='intent_set')
  final_tutor = models.ForeignKey(Tutor,related_name='matched_intent',blank=True,null=True,verbose_name='Matched tutor')
  ############# Auto Fields  ############
  last_edit_time = models.DateTimeField(auto_now=True,editable=True)

  ############# The old record part ##################
  if_confirmed = models.BooleanField(default=False,verbose_name=u"Tutor's Consent")
  startdate = models.DateField(u'Contract Signing Date',default=timezone.now,blank=True)
  chargedate = models.DateField(u'Commission Due Date',blank=True,null=True)
  service_fees = models.CharField(u'Total Commission Fee',blank=True,null=True,max_length=20)
  freq = models.CharField(u'Actual no. of lessons per week',blank=True,null=True,max_length=30)
  lesson_last = models.CharField(u'Actual no. of hours per lesson:(hours)',blank=True,null=True,max_length=30)
  lesson_price = models.CharField(u'Hourly Fee',blank=True,null=True,max_length=30)
  successful_match = models.BooleanField(u'Successful Match',default=False)
  commission_collection_status = models.BooleanField(u'Commission Collection Status',default=False)
  person_in_charge = models.CharField(u'Person in Charge',max_length=20,null=True,blank=True)
  failed = models.BooleanField(u'Failed',default=False)
  ################ close call ##################
  close_call_date = models.DateField(u'Close call date',null=True,blank=True)
  tuition_duration = models.CharField(u'Tuition frequency and duration',max_length=20,null=True,blank=True)
  OVERALLCOMMENT_CHOICES = (
    ('1','1 Star'),
    ('2','2 Star'),
    ('3','3 Star'),
    ('4','4 Star'),
    ('5','5 Star'),
  )
  overall_comment = models.CharField(u'Overall comment on the tutor',choices=OVERALLCOMMENT_CHOICES,default='1',max_length=10,null=True)
  q1 = models.TextField(u'Q1:What strength or wakness do you think your tutor has regarding the lessons?',null=True,blank=True)
  q2 = models.TextField(u'Q2:Anything you would like to complement or complain on your tutor in particular?',null=True,blank=True)
  self_evaluation = models.CharField(u'Tuition effect self-evaluation',choices=OVERALLCOMMENT_CHOICES,default='1',max_length=10,null=True)
  reasons = models.TextField(u'If feel no improvement, why?',null=True,blank=True)
  comment_charges = models.TextField(u'Comment on our charges',null=True,blank=True)
  RECOMMEND_CHOICES = (
    ("Yes","Yes"),
    ("Maybe","Maybe"),
    ('No','No')
  )
  recommend_or_not = models.CharField(u'Will he or she recommend us to his or her friend?',\
    max_length=10,choices=RECOMMEND_CHOICES,null=True,default='Yes')
  ################ close call end ##############


  def save(self, *args, **kwargs):
    super(StudentIntent, self).save(*args, **kwargs) # Call the "real" save() method.

    # Update the rank field automatically.
    self.student.intent_cnt += 1
    self.rank = self.student.intent_cnt
    self.student.save()

  #   super(StudentIntent, self).save(*args, **kwargs)
  def __str__(self):
    return "{}'s record".format(self.student.full_name)
class OptionalTutor(models.Model):
  record = models.ForeignKey(StudentIntent)
  tutor = models.ForeignKey(Tutor)
  tutor_consent = models.BooleanField(u'Tutor\'s consent',default=False)
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
# class Record(models.Model):
#   tutor = models.ForeignKey(Tutor,on_delete=models.CASCADE,related_name='records',limit_choices_to={'check':True})
#   student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='records')
#   if_confirmed = models.BooleanField(default=False,verbose_name=u"Tutor's Consent")
#   startdate = models.DateField(u'Contract Signing Date',default=timezone.now,blank=True)
#   chargedate = models.DateField(u'Commission Due Date',blank=True,null=True)
#   service_fees = models.CharField(u'Total Commission Fee',blank=True,null=True,max_length=20)
#   freq = models.CharField(u'Actual no. of lessons per week',blank=True,null=True,max_length=30)
#   lesson_last = models.CharField(u'Actual no. of hours per lesson:(hours)',blank=True,null=True,max_length=30)
#   lesson_price = models.CharField(u'Hourly Fee',blank=True,null=True,max_length=30)
#   successful_match = models.BooleanField(u'Successful Match',default=False)
#   commission_collection_status = models.BooleanField(u'Commission Collection Status',default=False)
#   #person_in_charge = models.CharField(u'Person in Charge',max_length=20,null=True,blank=True)
#   ################ close call ##################
#   close_call_date = models.DateField(u'Close call date',null=True,blank=True)
#   tuition_duration = models.CharField(u'Tuition duration',max_length=20,null=True,blank=True)
#   OVERALL_CHOICES = (
#     ('Very helpful','Very helpful'),
#     ('Not helping','Not helping')
#   )
#   overall_comment = models.CharField(u'Overall comment on the tutor',max_length=50\
#     ,choices=OVERALL_CHOICES,null=True,blank=True)
#   A1_CHOICES = (
#     ('Very well explained concepts','Very well explained concepts'),
#     ('Not very concise in the delivery','Not very concise in the delivery')
#   )
#   A2_CHOICES = (
#     ('Very boadrd knowledge','Very boadrd knowledge'),
#     ('Not very focused during tuition sessions','Very boadrd knowledge')
#   )
#   q1 = models.CharField(u'Q1:What strength or wakness do you think your tutor has regarding the lessons?',max_length=50\
#     ,choices=A1_CHOICES,null=True,blank=True)
  
#   q2 = models.CharField(u'Q2:Anything you would like to complement or complain on your tutor in particular?',max_length=50\
#     ,choices=A2_CHOICES,null=True,blank=True)
#   EVALUATION_CHOICES = (
#     ('Feel improved a lot','Feel improved a lot'),
#     ('Feel no improvement','Feel no improvement')
#   )
#   self_evaluation = models.CharField(u'Student\'s self evaluation',max_length=50,\
#     choices=EVALUATION_CHOICES,null=True,blank=True)
#   reasons = models.TextField(u'If feel no improvement, why?',null=True,blank=True)
#   comment_charges = models.CharField(u'Comment on our charges',max_length=100,null=True,blank=True)
#   RECOMMEND_CHOICES = (
#     ("Yes, would like to","Yes, would like to"),
#     ("Maybe","Maybe"),
#     ('No','No')
#   )
#   recommend_or_not = models.CharField(u'Will he or she recommend us to his or her friend?',\
#     max_length=50,choices=RECOMMEND_CHOICES,null=True,blank=True)
#   ################ close call end ##############
#   def save(self, *args, **kwargs):
#         super(Record, self).save(*args, **kwargs) # Call the "real" save() method.
#         self.tutor.save()

#   def __str__(self):
#     return 'student:{},tutor:{},firmed:{}'.format(self.student,self.tutor,self.if_confirmed)

class Feedback(models.Model):
  tutor = models.ForeignKey(Tutor,on_delete=models.CASCADE,related_name='feedbacks',limit_choices_to={'check':True})
  student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='feedbacks')
  subject = models.CharField(u'Subjects',max_length=50)
  attend = models.CharField(u'attendance',max_length=20) # if ontime = Yes, attend = On time, else attend = late_time
  record = models.OneToOneField(StudentIntent,related_name='feedback',null=True)
  # 5 aspects of evaluation:
  attitude = models.CharField(max_length=10)
  preparation = models.CharField(max_length=10)
  clarity = models.CharField(max_length=10)
  knowledgeability = models.CharField(max_length=10)
  outcome = models.CharField(max_length=10)
  # evaluation end
  
  time = models.FloatField(u'No. of Tuition Hours') # tuition_hour
  date = models.DateField(default=timezone.now)
  comment = models.TextField(u'Comment',blank=True)
  def save(self, *args, **kwargs):
    super(Feedback, self).save(*args, **kwargs) # Call the "real" save() method.
    self.tutor.save()

