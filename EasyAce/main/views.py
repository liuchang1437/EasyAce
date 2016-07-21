from django.shortcuts import render
from myAuth.models import Tutor,MyUser,Student
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from itertools import chain
from django.http import JsonResponse
import json
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
            messages.warning(request,'User didn\'t finish his/her information yet!')
            return HttpResponseRedirect('/index')
        if request.user.role=='student':
            student = request.user.get_user()
            return render(request, 'information_tutor.html', {'tutor':tutor,'student':student})
        return render(request, 'information_tutor.html', {'tutor':tutor})
    elif user.role=='student':
        student = user.get_user()
        if not student:
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
  if region:
    region1 = tutors.filter(region1__contains=region)
    region2 = tutors.filter(region2__contains=region)
    region3 = tutors.filter(region3__contains=region)
    tutors = region1 | region2 | region3
  if level:
    if subject and not subject=='Other':
      tutors = tutors.filter(prefer_teach__contains=subject)
    if subject and subject=='Other':
      tutors = tutors.filter(teaching_sub_other__contains=subject_other)
    else:
      tutors = tutors.filter(prefer_teach__contains=level)
  if gender:
    tutors = tutors.filter(gender=gender)
  return render(request, 'view_tutor.html', {'tutors':tutors})

def choose_tutor(request):
    if request.method == 'POST' and 'tutor_id' in request.POST:
        tutor_id = request.POST['tutor_id']
        user = request.user
        student = user.get_user()
        tutor = MyUser.objects.get(pk=tutor_id).get_user()
        if not student:
            messages.warning(request,'Please complete your info first.')
            return HttpResponseRedirect(reverse('myAuth:signup_tutor',\
            kwargs={'id':user.id}))
        student.tutors_chosen.add(tutor)
        student.save()
        data = {'added':True}
        return JsonResponse(data)
    else:
        return HttpResponseRedirect(reverse('main:index'))
def edit(request):
    user = request.user
    if user.role=='tutor':
        if request.method == 'POST':
            tutor = user.get_user()
            tutor.name = request.POST['name']
            tutor.gender = request.POST['gender']
            tutor.birth = request.POST['birthday']
            user.email = request.POST['email']
            tutor.phone = request.POST['phone']
            tutor.school = request.POST['school']
            tutor.wechat = request.POST['wechat']
            tutor.whatsapp = request.POST['whatsapp']
            # middle_test
            tutor.middle_test = request.POST['middle_test']
            middle_test_score = ''
            prefix = 'middle_sub'
            start = 1
            while(prefix+str(start) in request.POST):
                middle_test_score+=request.POST[prefix+str(start)]
                middle_test_score+=':'
                middle_test_score+=request.POST[prefix+str(start)+'_score']
                middle_test_score+=';'
                start+=1
            tutor.middle_test_score = middle_test_score
            # high_test
            high_test = request.POST['high_test']
            high_test_score = ''
            prefix = 'high_sub'
            start = 1
            while(prefix+str(start) in request.POST):
                high_test_score+=request.POST[prefix+str(start)]
                high_test_score+=':'
                high_test_score+=request.POST[prefix+str(start)+'_score']
                high_test_score+=';'
                start+=1
            tutor.high_test_score = high_test_score
            # prefer teach
            prefer_teach = ''
            prefix = 'teaching_'
            start = 1
            while(prefix+'level'+str(start) in request.POST):
                prefer_teach+=request.POST[prefix+'level'+str(start)]
                prefer_teach+=':'
                prefer_teach+=request.POST[prefix+'sub'+str(start)]
                prefer_teach+=';'
                start+=1
        
            regions = ''
            for i in range(1,4):
                regions+=request.POST['tutor_location_'+str(i)]
                regions+=';'
            region1 = request.POST('tutor_location_1')
            region2 = request.POST('tutor_location_2')
            region3 = request.POST('tutor_location_3')
            tutor.region1 = region1
            tutor.region2 = region2
            tutor.region3 = region3
            middle_sub_other = ''
            prefix = 'middle_sub'
            for i in range(1,10):
                if prefix+str(i)+'_other' in request.POST:
                    middle_sub_other+=request.POST[prefix+str(i)]
                    middle_sub_other+=','
                    middle_sub_other+=request.POST[prefix+str(i)+'_other']
                    middle_sub_other+=','
                    middle_sub_other+=request.POST[prefix+str(i)+'_score']
                    middle_sub_other+=';'
                    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1111')
                    print(request.POST[prefix+str(i)])
                    print(request.POST[prefix+str(i)+'_other'])
                    print(request.POST[prefix+str(i)+'_score'])
                    print(middle_sub_other)
            tutor.middle_sub_other = middle_sub_other
            high_sub_other = ''
            prefix = 'high_sub'
            for i in range(1,10):
                if prefix+str(i)+'_other' in request.POST:
                    high_sub_other+=request.POST[prefix+str(i)]
                    high_sub_other+=','
                    high_sub_other+=request.POST[prefix+str(i)+'_other']
                    high_sub_other+=','
                    high_sub_other+=request.POST[prefix+str(i)+'_score']
                    high_sub_other+=';'
            tutor.high_sub_other = high_sub_other
            teaching_sub_other = ''
            prefix = 'teaching_'
            for i in range(1,10):
                if prefix+'sub'+str(i)+'_other' in request.POST:
                    teaching_sub_other += request.POST[prefix+'level'+str(i)]
                    teaching_sub_other += ','
                    teaching_sub_other += request.POST[prefix+'sub'+str(i)]
                    teaching_sub_other += ','
                    teaching_sub_other += request.POST[prefix+'sub'+str(i)+'_other']
                    teaching_sub_other += ';'
                    prefer_teach += request.POST[prefer+'sub'+str(i)]
                    prefer_teach +=':'
                    prefer_teach += request.POST[prfer+'sub'+str(i)+'_other']
                    prefer_teach += ';'
            if 'photo' in request.FILES:
                tutor.photo=request.FILES['photo']
            tutor.prefer_teach = prefer_teach
            tutor.teaching_sub_other = teaching_sub_other
            tutor.regions = regions
            tutor.duration = request.POST['teach_duration']
            tutor.num_taught = request.POST['num_taught']
            tutor.achievement = request.POST['achievement']
            tutor.save()
            user.save()
            messages.success(request,'Update information successfully!')
            return HttpResponseRedirect('/index')
        else:
            tutor = user.get_user()
            if tutor:
                middle_test_score = tutor.get_pairs('middle_test_score')
                high_test_score = tutor.get_pairs('high_test_score')
                prefer_teach = tutor.get_pairs('prefer_teach')
                regions = tutor.get_single('regions')
                middle_sub_other = tutor.get_triple('middle_sub_other')
                high_sub_other = tutor.get_triple('high_sub_other')
                teaching_sub_other = tutor.get_triple('teaching_sub_other')
                return render(request,'signup_tutor.html',{'id':user.id,'edit':True,'tutor':tutor,\
                        'middle_test_score':middle_test_score,'high_test_score':high_test_score,\
                        'prefer_teach':prefer_teach,'regions':regions,\
                        'middle_sub_other':middle_sub_other,'high_sub_other':high_sub_other,\
                        'teaching_sub_other':teaching_sub_other})
            return HttpResponseRedirect(reverse('myAuth:signup_tutor',kwargs={'id':user.id}))
    else:
        if request.method == 'POST':
            student = user.get_user()
            student.name = request.POST['name']
            student.gender = request.POST['gender']
            #birth = request.POST['birthday']
            user.email = request.POST['email']
            student.phone = request.POST['phone']
            student.school = request.POST['school']
            student.wechat = request.POST['wechat']
            student.whatsapp = request.POST['whatsapp']
            student.grade = request.POST['grade']
            student.location = request.POST['student_location']
            student.loc_nego = request.POST['student_location_negotiable']
            student.exam_type = request.POST['student_subject']    
            # subjects
            subjects = ''
            prefix = 'student_subject'
            start = 1
            while(prefix+str(start) in request.POST):
                subjects+=request.POST[prefix+str(start)]
                subjects+=';'
                start+=1
            student.subjects = subjects
            student.duration_per_lesson = request.POST['student_duration_per_lesson']
            student.start_time = request.POST['student_start_time']
            student.lesson_per_week = request.POST['student_lesson_per_week']
            student.prefer_tutor = request.POST['student_tutor_preference']
            # remarks
            remarks=''
            prefix = 'student_remark'
            for i in range(1,7):
                if prefix+str(i) in request.POST:
                    remarks+=request.POST[prefix+str(i)]
                    remarks+=';'
            student.remarks = remarks
            # subjects other
            subjects_other=''
            prefix = 'student_subject'
            for i in range(1,11):
                if prefix+str(i)+'_other' in request.POST:
                    subjects_other+=request.POST[prefix+str(i)+'_other']
                    subjects_other+=';'
            student.subjects_other = subjects_other
            student.weakness = request.POST['student_weakness']
            if student.start_time=='Other':
                start_time_other = request.POST['student_start_time_other']
                student.start_time_other = start_time_other
            student.save()
            user.save()
            # print(student.subjects_other)
            # print(student.start_time_other)
            # print(student.remarks)
            messages.success(request,'Update information successfully!')
            return HttpResponseRedirect('/index')
        else:
            student = user.get_user()
            if student:
                remarks = student.get_single('remarks')
                subjects = student.get_single('subjects')
                subjects_other = student.get_single('subjects_other')
                return render(request,'signup_student.html',{'edit':True,'id':user.id,'student':student,\
                'remarks':remarks,'subjects':subjects,'subjects_other':subjects_other})
            return HttpResponseRedirect(reverse('myAuth:signup_student',kwargs={'id':user.id}))

def edit_student(request):
    user = request.user
    if request.method == 'POST':
        student = user.get_user()
        subjects = student.get_single('subjects')
        subjects_other = student.get_single('subjects_other')
        exam_type = student.exam_type
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
        middle_test = tutor.middle_test
        high_test = tutor.high_test
        middle_test_score = tutor.get_pairs('middle_test_score')
        high_test_score = tutor.get_pairs('high_test_score')
        prefer_teach = tutor.get_prefer_teach()
        middle_sub_other = tutor.get_triple('middle_sub_other')
        high_sub_other = tutor.get_triple('high_sub_other')
        teaching_sub_other = tutor.get_triple('teaching_sub_other')

        data = {}
        data["middle_test"] = middle_test
        data["high_test"] = high_test
        data["middle_test_score"] = middle_test_score
        data["high_test_score"] = high_test_score
        data["prefer_teach"] = prefer_teach
        data["middle_sub_other"] = middle_sub_other
        data["high_sub_other"] = high_sub_other
        data["teaching_sub_other"] = teaching_sub_other
        data_json = json.dumps(data)
        print(data_json)
        return JsonResponse(data_json, safe=False)





