from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import LoginForm,SignupForm
from .models import MyUser,Tutor, Student
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login(request):
  next = request.GET.get('next') or ''
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username,password=password)
    if user is not None:
      if user.is_active:
        login_user(request,user)
        messages.success(request,'Log in successfully!')
        if request.POST['next']!='':
          next = request.POST['next']
          return HttpResponseRedirect(next)
        return HttpResponseRedirect('/index')
      else:
        message.error(request,'The account has been disabled!')
        return HttpResponseRedirect('myAuth:login')
    else:
      messages.error(request,'The username and password were inccorect.')
      return HttpResponseRedirect(reverse('myAuth:login'))
  return render(request,'login.html',{'next':next})

def signup(request):
  if request.method=='POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      role = form.cleaned_data['role']
      password = form.cleaned_data['password']
      user = MyUser.objects.create_user(username=username,role=role,password=password)
      user.save()
      user = authenticate(username=username,password=password)
      login_user(request,user)
      messages.success(request,'You have signed up successfully! Please log in and complete some further information.')
      if role=='tutor':
        return HttpResponseRedirect(reverse('myAuth:signup_tutor',kwargs={'id':user.id}))
      else:
        return HttpResponseRedirect(reverse('myAuth:signup_student',kwargs={'id':user.id}))
    messages.error(request,'Please fill in all the fields!')
    return HttpResponseRedirect(reverse('myAuth:signup'))
  else:
    form = SignupForm()
    return render(request,'signup.html',{'form':form})
@login_required
def logout(request):
  logout_user(request)
  messages.success(request,'Log out successfully!')
  return HttpResponseRedirect('/index')

@login_required
def signup_tutor(request,id):
  if request.method == 'POST':
    name = request.POST['name']
    gender = request.POST['gender']
    birth = request.POST['birthday']
    email = request.POST['email']
    phone = request.POST['phone']
    school = request.POST['school']
    wechat = request.POST['wechat']
    whatsapp = request.POST['whatsapp']
    # middle_test
    middle_test = request.POST['middle_test']
    middle_test_score = ''
    prefix = 'middle_sub'
    start = 1
    while(prefix+str(start) in request.POST):
      middle_test_score+=request.POST[prefix+str(start)]
      middle_test_score+=':'
      middle_test_score+=request.POST[prefix+str(start)+'_score']
      middle_test_score+=';'
      start+=1
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
    duration = request.POST['teach_duration']
    num_taught = request.POST['num_taught']
    achievement = request.POST['achievement']
    myuser = MyUser.objects.filter(id=id)[0]
    myuser.email = email
    tutor = Tutor(name=name,gender=gender,phone=phone,birth=birth,\
      school=school,wechat=wechat,whatsapp=whatsapp,middle_test=middle_test,\
      middle_test_score=middle_test_score,high_test=high_test,\
      high_test_score=high_test_score,regions=regions,duration=duration,\
      num_taught=num_taught,achievement=achievement,prefer_teach=prefer_teach)
    tutor.base_info = myuser
    tutor.save()
    messages.success(request,'Update information successfully!')
    return HttpResponseRedirect('/index')
  else:
    user = MyUser.objects.filter(id=id)[0]
    tutor = user.get_user()
    if tutor:
      middle_test_score = tutor.get_pairs('middle_test_score')
      high_test_score = tutor.get_pairs('high_test_score')
      prefer_teach = tutor.get_pairs('prefer_teach')
      regions = tutor.get_single('regions')
      return render(request,'signup_tutor.html',{'id':id,'tutor':tutor,\
            'middle_test_score':middle_test_score,'high_test_score':high_test_score,\
            'prefer_teach':prefer_teach,'regions':regions})
    return render(request, 'signup_tutor.html',{'id':id})

@login_required
def signup_student(request,id):
  if request.method == 'POST':
    name = request.POST['name']
    gender = request.POST['gender']
    #birth = request.POST['birthday']
    email = request.POST['email']
    phone = request.POST['phone']
    school = request.POST['school']
    wechat = request.POST['wechat']
    whatsapp = request.POST['whatsapp']
    grade = request.POST['grade']
    location = request.POST['student_location']
    loc_nego = request.POST['student_location_negotiable']
    exam_type = request.POST['student_subject']    
    # subjects
    subjects = ''
    prefix = 'student_subject'
    start = 1
    while(prefix+str(start) in request.POST):
      subjects+=request.POST[prefix+str(start)]
      subjects+=';'
      start+=1
    
    duration_per_lesson = request.POST['student_duration_per_lesson']
    start_time = request.POST['student_start_time']
    lesson_per_week = request.POST['student_lesson_per_week']
    prefer_tutor = request.POST['student_tutor_preference']
    # remarks
    remarks=''
    prefix = 'student_remark'
    start = 1
    while(prefix+str(start) in request.POST):
      remarks+=request.POST[prefix+str(start)]
      remarks+=';'
      start+=1
    weakness = request.POST['student_weakness']
    myuser = MyUser.objects.filter(id=id)[0]
    myuser.email = email
    student = Student(name=name,gender=gender,phone=phone,\
      school=school,wechat=wechat,whatsapp=whatsapp,grade=grade,location=location,\
      loc_nego=loc_nego,exam_type=exam_type,subjects=subjects,\
      duration_per_lesson=duration_per_lesson,start_time=start_time,\
      lesson_per_week=lesson_per_week,prefer_tutor=prefer_tutor,\
      weakness=weakness,remarks=remarks)
    student.base_info = myuser
    student.save()
    messages.success(request,'Update information successfully!')
    return HttpResponseRedirect('/index')
  else:
    user = MyUser.objects.filter(id=id)[0]
    student = user.get_user()
    if student:
      remarks = student.get_single('remarks')
      subjects = student.get_single('subjects')
      return render(request,'signup_tutor.html',{'id':id,'student':student,\
        'remarks':remarks,'subjects':subjects})
    return render(request, 'signup_student.html',{'id':id})