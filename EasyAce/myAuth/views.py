from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import LoginForm,SignupForm
from .models import MyUser,Tutor, Student, PreferSubject, StudentPreferSub,ReferSubject
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
      messages.success(request,'You have signed up successfully! Please complete some further information.')
      if role=='tutor':
        return HttpResponseRedirect(reverse('myAuth:signup_tutor'))
      else:
        return HttpResponseRedirect(reverse('myAuth:signup_student'))
    messages.error(request,'The username you used already exists!')
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
def signup_tutor(request):
  if request.method == 'POST':
    if request.user.get_user():
      messages.error(request,'The user has existed!')
      return HttpResponseRedirect('/index')
    #### Base info start
    name = request.POST['name']
    gender = request.POST['gender']
    birth = request.POST['birthday']
    email = request.POST['email']
    phone = request.POST['phone']
    school = request.POST['school']
    wechat = request.POST['wechat']
    whatsapp = request.POST['whatsapp']
    #### Base info end

    #### Profile start
    teach_duration = request.POST['teach_duration']
    num_taught = request.POST['num_taught']
    achievement = request.POST['achievement']
    #### Profile end

    #### Create tutor start
    myuser = request.user
    myuser.email = email
    myuser.save()
    tutor = Tutor(username=myuser.username,name=name,gender=gender,phone=phone,birth=birth,\
      school=school,wechat=wechat,whatsapp=whatsapp,email=email,\
      teach_duration=teach_duration,num_taught=num_taught,achievement=achievement,\
      base_info=myuser)
    if 'photo' in request.FILES:
      tutor.photo = request.FILES['photo']
    if 'tutor_location_1' in request.POST:
      tutor.tutor_location1 = request.POST['tutor_location_1']
    if 'tutor_location_2' in request.POST:
      tutor.tutor_location2 = request.POST['tutor_location_2']
    if 'tutor_location_3' in request.POST:
      tutor.tutor_location3 = request.POST['tutor_location_3']
    tutor.save()
    #### Create tutor end

    #### Start create prefer teach and refer teach 
    for i in range(1,10):
      if 'teach_level'+str(i) in request.POST:
        level = request.POST['teach_level'+str(i)]
        name = request.POST['teach_sub'+str(i)]
        other = request.POST['teach_sub_other'+str(i)]
        prefer_teach = PreferSubject(level=level,name=name,rank=i,other=other,\
          tutor=tutor)
        prefer_teach.save()
      if 'ref_level'+str(i) in request.POST:
        level = request.POST['ref_level'+str(i)]
        name = request.POST['ref_sub'+str(i)]
        other = request.POST['ref_sub_other'+str(i)]
        score = request.POST['ref_score'+str(i)]
        refer_teach = ReferSubject(level=level,name=name,score=score,rank=i,\
          other=other,tutor=tutor)
        refer_teach.save()
    #### END
    tutor.cal_isr()
    tutor.save()
    messages.success(request,'Update information successfully!')
    return HttpResponseRedirect('/index')
  else:
    return render(request, 'signup_tutor.html')

@login_required
def signup_student(request):
  if request.method == 'POST':
    if request.user.get_user():
      messages.error(request,'The user has existed!')
      return HttpResponseRedirect('/index')
    #### Base info start
    name = request.POST['name']
    gender = request.POST['gender']
    email = request.POST['email']
    phone = request.POST['phone']
    school = request.POST['school']
    grade = request.POST['grade']
    wechat = request.POST['wechat']
    whatsapp = request.POST['whatsapp']
    #### Base info end

    #### Preference start
    location = request.POST['student_location']
    loc_nego = request.POST['student_location_negotiable']
    time_per_lesson = request.POST['student_duration_per_lesson']
    lesson_per_week = request.POST['student_lesson_per_week']
    start_time = request.POST['student_start_time']
    prefer_tutor_gender = request.POST['student_tutor_preference']
    #### Preference end

    #### Create student start
    myuser = request.user
    myuser.email = email
    myuser.save()
    student = Student(username=myuser.username,name=name,gender=gender,\
      email=email,phone=phone,school=school,grade=grade,\
      wechat=wechat,whatsapp=whatsapp,base_info=myuser,\
      location=location,loc_nego=loc_nego,\
      time_per_lesson=time_per_lesson,start_time=start_time,\
      lesson_per_week=lesson_per_week,prefer_tutor_gender=prefer_tutor_gender)
    if start_time=='Other':
      student.start_time_other = request.POST['student_start_time_other']
    remarks=''
    prefix = 'student_remark'
    for i in range(1,7):
      if prefix+str(i) in request.POST:
        remarks+=request.POST[prefix+str(i)]
        remarks+=';'
    student.remarks=remarks
    if 'weakness' in request.POST:
      student.weakness = request.POST['student_weakness']
    student.save()
    #### Create student end

    #### Start create prefer teach and refer teach
    student_subject = request.POST['student_subject'] 
    for i in range(1,10):
      if 'student_subject'+str(i) in request.POST:
        name = request.POST['student_subject'+str(i)]
        other = False
        if 'student_subject'+str(i)+'_other' in request.POST:
          other = request.POST['student_subject'+str(i)+'_other']
        prefer_sub = StudentPreferSub(level=student_subject,name=name,rank=i,other=other,\
          student=student)
        prefer_sub.save()
    #### END

    messages.success(request,'Update information successfully!')
    return HttpResponseRedirect('/index')
  else:
    return render(request, 'signup_student.html')
