from django.shortcuts import render
from myAuth.models import Tutor,MyUser,Student,PreferSubject,ReferSubject,\
    StudentPreferSub, Feedback, StudentIntent
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'index.html')
def information_tutor(request,id):
    tutors = Tutor.objects.filter(id=id)
    print(tutors)
    return render(request, 'information_tutor.html', {'tutors':tutors})
def information(request,id):
    try:
        user = MyUser.objects.get(pk=id)
    except ObjectDoesNotExist:
        messages.error(request,'User does not exist!')
        return HttpResponseRedirect('/index')
    if user.role=='tutor':
        tutor = user.get_user()
        if not tutor:
            if user==request.user:
                messages.warning(request,'Please complete your information first!')
                return HttpResponseRedirect(reverse('myAuth:signup_tutor'))
            messages.warning(request,'User didn\'t finish his/her information yet!')
            return HttpResponseRedirect('/index')
        if request.user.is_authenticated() and request.user.role=='student':
            student = request.user.get_user()
            return render(request, 'information_tutor.html', {'tutor':tutor,'student':student})
        return render(request, 'information_tutor.html', {'tutor':tutor})
    elif user.role=='student':
        student = user.get_user()
        if not student:
            if user==request.user:
                messages.warning(request,'Please complete your information first!')
                return HttpResponseRedirect(reverse('myAuth:signup_student'))
            messages.warning(request,'User didn\'t finish his/her information yet!')
            return HttpResponseRedirect('/index')
        return render(request, 'information_student.html', {'student':student})
    else:
        messages.error(request,'User didn\'t finish his/her information yet!')
        return HttpResponseRedirect('/index')

def view_tutor(request):
  region = request.GET.get('region')
  level = request.GET.get('level')
  subject = request.GET.get('subject')
  subject_other = request.GET.get('subject_other')
  gender = request.GET.get('gender')
  tutors = Tutor.objects.filter(check=True)
  if region!='All':
    region1 = tutors.filter(tutor_location1__contains=region)
    region2 = tutors.filter(tutor_location2__contains=region)
    region3 = tutors.filter(tutor_location3__contains=region)
    tutors = region1 | region2 | region3
  if level!='All':
      tutors = tutors.filter(prefer_sub__level=level)
  if subject!='All':
      tutors = tutors.filter(prefer_sub__name=subject)
  if gender!='All':
    tutors = tutors.filter(gender=gender)
  paginator = Paginator(tutors,30)
  page = request.GET.get('page')
  try:
    tutors = paginator.page(page)
  except PageNotAnInteger:
    tutors = paginator.page(1)
  except EmptyPage:
    tutors = paginator.page(paginator.num_pages)
  return render(request, 'view_tutor.html', {'tutors':tutors})

def choose_tutor(request):
    if request.method == 'POST' and 'tutor_id' in request.POST:
        tutor_id = request.POST['tutor_id']
        user = request.user
        student = user.get_user()
        tutor = MyUser.objects.get(pk=tutor_id).get_user()
        if not student:
            messages.warning(request,'Please complete your info first.')
            return HttpResponseRedirect(reverse('myAuth:signup_student'))
        print('here')
        student.tutors_chosen.add(tutor)
        student.save()
        data = {'added':True}
        return JsonResponse(data)
    else:
        return HttpResponseRedirect(reverse('main:index'))
@login_required
def remove_intent(request):
    if request.method == 'POST' and 'id' in request.POST:
        intent_id = request.POST['id']
        intent = StudentIntent.objects.get(pk=intent_id)
        intent.delete()
        data = {'removed':True}
        return JsonResponse(data)
    else:
        return HttpResponseRedirect(reverse('main:information',kwargs={'id':request.user.id}))
def edit(request):
    user = request.user
    # if the user is a tutor.
    if user.role=='tutor':
        # if post the form, update the information
        if request.method == 'POST':
            tutor = user.get_user()
            #### Base info start
            tutor.name = request.POST['name']
            tutor.gender = request.POST['gender']
            tutor.birth = request.POST['birthday']
            tutor.email = request.POST['email']
            tutor.phone = request.POST['phone']
            tutor.school = request.POST['school']
            tutor.wechat = request.POST['wechat']
            tutor.whatsapp = request.POST['whatsapp']
            #### Base info end

            #### Profile start
            tutor.teach_duration = request.POST['teach_duration']
            tutor.num_taught = request.POST['num_taught']
            tutor.achievement = request.POST['achievement']
            #### Profile end

            #### Option fields start
            user.email = request.POST['email']
            user.save()
            if 'photo' in request.FILES:
                tutor.photo = request.FILES['photo']
            if 'tutor_location_1' in request.POST:
                tutor.tutor_location1 = request.POST['tutor_location_1']
            if 'tutor_location_2' in request.POST:
                tutor.tutor_location2 = request.POST['tutor_location_2']
            if 'tutor_location_3' in request.POST:
                tutor.tutor_location3 = request.POST['tutor_location_3']
            tutor.save()
            #### Option fields end

            #### Start create prefer teach and refer teach 
            for sub in tutor.prefer_subs.all():
                sub.delete()
            for sub in tutor.refer_subs.all():
                sub.delete()
            for i in range(1,10):
                if 'teach_level'+str(i) in request.POST:
                    level = request.POST['teach_level'+str(i)]
                    name = request.POST['teach_sub'+str(i)]
                    other = False
                    if name == "Other":
                        name = request.POST['teach_sub_other'+str(i)]
                        other = True
                    prefer_teach = PreferSubject(level=level,name=name,rank=i,other=other,\
                        tutor=tutor)
                    prefer_teach.save()
                if 'ref_level'+str(i) in request.POST:
                    level = request.POST['ref_level'+str(i)]
                    name = request.POST['ref_sub'+str(i)]
                    other = False
                    if name == "Other":
                        name = request.POST['ref_sub_other'+str(i)]
                        other = True
                    score = request.POST['ref_score'+str(i)]
                    refer_teach = ReferSubject(level=level,name=name,score=score,rank=i,\
                        other=other,tutor=tutor)
                    refer_teach.save()
            #### END
            #print(tutor.isr)
            tutor.save()
            messages.success(request,'Update information successfully!')
            return HttpResponseRedirect(reverse('main:information',kwargs={'id':user.id}))
            # End update information
        # if the method is GET, offer old information
        else:
            tutor = user.get_user()
            if tutor:
                return render(request,'signup_tutor.html',{'tutor':tutor,'edit':True})
            return HttpResponseRedirect(reverse('myAuth:signup_tutor'))
    # the user is a student
    else:
        # If post the form, update student info.
        if request.method == 'POST':
            student = user.get_user()
            #### Base info start
            student.name = request.POST['name']
            student.gender = request.POST['gender']
            student.email = request.POST['email']
            student.phone = request.POST['phone']
            student.school = request.POST['school']
            student.grade = request.POST['grade']
            student.wechat = request.POST['wechat']
            student.whatsapp = request.POST['whatsapp']
            #### Base info end

            #### Preference start
            student.location = request.POST['student_location']
            student.loc_nego = request.POST['student_location_negotiable']
            student.time_per_lesson = request.POST['student_duration_per_lesson']
            student.lesson_per_week = request.POST['student_lesson_per_week']
            student.start_time = request.POST['student_start_time']
            student.prefer_tutor_gender = request.POST['student_tutor_preference']
            #### Preference end

            #### Option fields start
            user.email = request.POST['email']
            user.save()
            if request.POST['student_start_time']=='Other':
                student.start_time_other = request.POST['student_start_time_other']
            remarks=''
            prefix = 'student_remark'
            for i in range(1,7):
                if prefix+str(i) in request.POST:
                    remarks+=request.POST[prefix+str(i)]
                    remarks+=';'
            student.remarks=remarks
            if 'student_weakness' in request.POST:
                student.weakness = request.POST['student_weakness']
            student.save()
            #### Option fields end

            #### Start create prefer teach and refer teach
            student_subject = request.POST['student_subject']
            for sub in student.prefer_subs.all():
                sub.delete() 
            for i in range(1,10):
                if 'student_subject'+str(i) in request.POST:
                    name = request.POST['student_subject'+str(i)]
                    other = False
                    if name == "Other":
                        name = request.POST['student_subject'+str(i)+'_other']
                        other = True
                    prefer_sub = StudentPreferSub(level=student_subject,name=name,rank=i,other=other,\
                        student=student)
                    prefer_sub.save()
            #### END
            messages.success(request,'Update information successfully!')
            return HttpResponseRedirect(reverse('main:information',kwargs={'id':user.id}))
        # if method is GET
        else:
            student = user.get_user()
            if student:
                return render(request,'signup_student.html',{'student':student,'edit':True})
            return HttpResponseRedirect(reverse('myAuth:signup_student'))

def edit_student(request):
    user = request.user
    if request.method == 'POST':
        student = user.get_user()
        exam_type = student.prefer_subs.all()[0].level
        subjects = []
        subjects_other = []
        for sub in student.prefer_subs.all():
            subjects.append(sub.name)
            subjects_other.append(sub.other)
        data = {}
        data["exam_type"] = exam_type
        data['subjects'] = subjects
        data['subjects_other'] = subjects_other
        data_json = json.dumps(data)
        print(data_json)
        return JsonResponse(data_json, safe=False)

def edit_tutor(request):
    user = request.user
    if request.method == 'POST':
        tutor = user.get_user()
        prefer_level = []
        prefer_other = []
        prefer_name = []
        refer_level = []
        refer_other = []
        refer_name = []
        refer_score =[]

        for sub in tutor.prefer_subs.all():
            prefer_level.append(sub.level)
            prefer_other.append(sub.other)
            prefer_name.append(sub.name)
        for sub in tutor.refer_subs.all():
            refer_level.append(sub.level)
            refer_other.append(sub.other)
            refer_name.append(sub.name)
            refer_score.append(sub.score)
        

        data = {}
        data["prefer_level"] = prefer_level
        data["prefer_other"] = prefer_other
        data["prefer_name"] = prefer_name
        data["refer_level"] = refer_level
        data["refer_name"] = refer_name
        data["refer_other"] = refer_other
        data["refer_score"] = refer_score

        # 对象数组
        #data["prefer_subs"] = tutor.prefer_subs.all()
        #data["refer_subs"] = tutor.refer_subs.all()
        # End
        data_json = json.dumps(data)
        print(data_json)
        return JsonResponse(data_json, safe=False)
def feedback(request,record_id):
    student = request.user.get_user()
    if request.method == 'POST':
        #record = Record.objects.get(pk=record_id)
        feedback = Feedback()
        feedback.tutor = record.tutor
        feedback.student = student
        feedback.subject = request.POST['subject']
        if request.POST['ontime'] == 'Yes':
            feedback.attend = 'On time'
        else:
            feedback.attend = request.POST['late_time']
        feedback.attitude = request.POST['attitude']
        feedback.preparation = request.POST['preparation']
        feedback.clarity = request.POST['clarity']
        feedback.knowledgeability = request.POST['knowledgeability']
        feedback.outcome = request.POST['outcome']
        feedback.time = request.POST['tuition_hour']
        feedback.comment = request.POST['comment']
        feedback.save()
        messages.info(request,'Submit feedback successfully! Thank you for that.')
        return HttpResponseRedirect(reverse('main:information',kwargs={'id':request.user.id}))
    return render(request, 'feedback.html')
def add_intent(request):
    tutor = request.GET.get('tutor') or ''
    if tutor:
        tutor = MyUser.objects.get(pk=tutor)
    if request.method == 'POST':
        student = request.user.get_user()
        if not student or request.user.role=='tutor':
            messages.error(request,"Sorry, but it seems that you are not a student.")
            return HttpResponseRedirect(reverse('main:index'))    
        # must fill
        intent_level = request.POST['intent_level']
        intent_subject = request.POST['intent_subject']
        intent_duration_per_lesson = request.POST['intent_duration_per_lesson']
        intent_lesson_per_week = request.POST['intent_lesson_per_week']
        intent_start_time = request.POST['intent_start_time']
        intent = StudentIntent(intent_level=intent_level,intent_subject=intent_subject,\
            intent_duration_per_lesson=intent_duration_per_lesson,\
            intent_lesson_per_week=intent_lesson_per_week,\
            intent_start_time=intent_start_time,student=student)

        # don't must to fill those
        if intent_subject =='Other':
            intent.intent_subject = request.POST['intent_subject_other']
            intent.intent_subject_other = True
        if intent_start_time == 'Other':
            intent.intent_start_time_other = request.POST['intent_start_time_other']
        if 'intent_remark1' in request.POST:
            intent.intent_remark1 = request.POST['intent_remark1']
        if 'intent_remark2' in request.POST:
            intent.intent_remark2 = request.POST['intent_remark2']
        if 'intent_remark3' in request.POST:
            intent.intent_remark3 = request.POST['intent_remark3']
        if 'intent_remark4' in request.POST:
            intent.intent_remark4 = request.POST['intent_remark4']
        if 'intent_remark5' in request.POST:
            intent.intent_remark5 = request.POST['intent_remark5']
        if 'intent_remark6' in request.POST:
            intent.intent_remark6 = request.POST['intent_remark6']
        if 'intent_weakness' in request.POST:
            intent.intent_weakness = request.POST['intent_weakness']
        if tutor:
            intent.intent_tutor = tutor
        intent.save()

        messages.success(request,'Add an intent successfully!')
        return HttpResponseRedirect(reverse('main:information',kwargs={'id':request.user.id}))
    else:
        return render(request,'intent_student.html',{'tutor':tutor})



