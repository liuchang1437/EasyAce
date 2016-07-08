from django.shortcuts import render
from myAuth.models import Tutor,MyUser,Student
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
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
            messages.warning(request,'Please complete your info first.')
            return HttpResponseRedirect(reverse('myAuth:signup_tutor',\
            kwargs={'id':user.id}))
        middle_test_score = tutor.get_pairs('middle_test_score')
        high_test_score = tutor.get_pairs('high_test_score')
        prefer_teach = tutor.get_pairs('prefer_teach')
        regions = tutor.get_single('regions')
        print(middle_test_score)
        return render(request, 'information_tutor.html', {'tutor':tutor,\
            'middle_test_score':middle_test_score,'high_test_score':high_test_score,\
            'prefer_teach':prefer_teach,'regions':regions})
    elif user.role=='student':
        student = user.get_user()
        if not student:
            messages.warning(request,'Please complete your info first.')
            return HttpResponseRedirect(reverse('myAuth:signup_tutor',\
            kwargs={'id':user.id}))
        remarks = student.get_single('remarks')
        subjects = student.get_single('subjects')
        subjects_other = student.get_single('subjects_other')
        return render(request, 'information_student.html', {'student':student,\
            'remarks':remarks,'subjects':subjects,'subjects_other':subjects_other})
    else:
        return render(request, 'index.html')

def view_tutor(request):
    regions = request.GET.get('r')
    # = request.GET.get('')
    if regions:
        tutors = Tutor.objects.filter(regions__contains=regions)
    else:
        tutors = Tutor.objects.all()
    return render(request, 'view_tutor.html', {'tutors':tutors})

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
            tutor.prefer_teach = prefer_teach
            regions = ''
            for i in range(1,4):
                regions+=request.POST['tutor_location_'+str(i)]
                regions+=';'
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
                return render(request,'edit_tutor.html',{'id':user.id,'tutor':tutor,\
                        'middle_test_score':middle_test_score,'high_test_score':high_test_score,\
                        'prefer_teach':prefer_teach,'regions':regions})
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
                return render(request,'edit_student.html',{'id':user.id,'student':student,\
                'remarks':remarks,'subjects':subjects,'subjects_other':subjects_other})
            return HttpResponseRedirect(reverse('myAuth:signup_student',kwargs={'id':user.id}))