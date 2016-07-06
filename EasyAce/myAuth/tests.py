from django.test import TestCase

# Create your tests here.
from .models import MyUser,Tutor,Student

def create_tutor(base_info,name='name',gender='gender',phone='phone',birth='1994-02-17',\
      school='school',wechat='wechat',whatsapp='whatsapp',middle_test='middle_test',\
      middle_test_score='middle_test_score',high_test='high_test',\
      high_test_score='high_test_score',regions='regions',duration='duration',\
      num_taught='num_taught',achievement='achievement',prefer_teach='prefer_teach'):
      return Tutor.objects.create(base_info=base_info,name=name,gender=gender,\
        phone=phone,birth=birth,school=school,wechat=wechat,whatsapp=whatsapp,\
        middle_test=middle_test,middle_test_score=middle_test_score,high_test=high_test,\
        high_test_score=high_test_score,regions=regions,duration=duration,\
        num_taught=num_taught,achievement=achievement,prefer_teach=prefer_teach)
def create_student(base_info,name='name',gender='gender',phone='phone',\
      school='school',wechat='wechat',whatsapp='whatsapp',grade='grade',location='location',\
      loc_nego='loc_nego',exam_type='exam_type',subjects='subjects',\
      duration_per_lesson='duration_per_lesson',start_time='start_time',\
      lesson_per_week='lesson_per_week',prefer_tutor='prefer_tutor',\
      weakness='weakness',remarks='remarks'):
      return Student.objects.create(base_info=base_info,name=name,gender=gender,\
        phone=phone,school=school,wechat=wechat,whatsapp=whatsapp,grade=grade,\
        location=location,loc_nego=loc_nego,exam_type=exam_type,subjects=subjects,\
        duration_per_lesson=duration_per_lesson,start_time=start_time,\
        lesson_per_week=lesson_per_week,prefer_tutor=prefer_tutor,\
        weakness=weakness,remarks=remarks)
class MyUserModelTest(TestCase):
  def test_get_user(self):
    """
     MyUser.get_user() should return the extra_info model according to the role of the
    user.
    """
    tutor_user = MyUser.objects.create(username='test',password='test',role='tutor')
    tutor_user1 = MyUser.objects.create(username='test1',password='test',role='tutor')
    student_user = MyUser.objects.create(username='test2',password='test',role='student')
    student_user2 = MyUser.objects.create(username='test3',password='test',role='S')
    
    tutor = create_tutor(tutor_user)
    student = create_student(student_user)

    self.assertEqual(tutor_user.get_user(),tutor)
    self.assertEqual(student_user.get_user(),student)
    self.assertEqual(tutor_user1.get_user(),False) # 还未创建额外信息
    
    student2 = create_student(tutor_user1)
    self.assertEqual(tutor_user1.get_user(),False) # role 不匹配
    self.assertEqual(student_user2.get_user(),False) # role 错误
# class TutorModelTest(TestCase):
#   def test_return_pairs(self):
#     """
#       return_pairs(self,field_name) should return pairs.And the field_name should be in
#     the form of "n1:v1;n2:v2;..."
#     """
#     user = MyUser.objects.create(username='test',password='test',role='tutor')
#     tutor = create_tutor()