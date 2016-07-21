from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import LoginForm,SignupForm
from .models import MyUser,Tutor, Student, PreferSubject, ReferSubject
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
    for i in range(1,7):
      if prefix+str(i) in request.POST:
        remarks+=request.POST[prefix+str(i)]
        remarks+=';'
    # subjects other
    subjects_other=''
    prefix = 'student_subject'
    for i in range(1,11):
      if prefix+str(i)+'_other' in request.POST:
        subjects_other+=request.POST[prefix+str(i)+'_other']
        subjects_other+=';'
    weakness = request.POST['student_weakness']
    myuser = MyUser.objects.filter(id=id)[0]
    myuser.email = email
    student = Student(name=name,gender=gender,phone=phone,\
      school=school,wechat=wechat,whatsapp=whatsapp,grade=grade,location=location,\
      loc_nego=loc_nego,exam_type=exam_type,subjects=subjects,\
      duration_per_lesson=duration_per_lesson,start_time=start_time,\
      lesson_per_week=lesson_per_week,prefer_tutor=prefer_tutor,\
      weakness=weakness,remarks=remarks,subjects_other=subjects_other,email=email,username=myuser.username)
    if start_time=='Other':
      start_time_other = request.POST['student_start_time_other']
      student.start_time_other = start_time_other
    student.base_info = myuser
    student.save()
    myuser.save()
    # print(student.subjects_other)
    # print(student.start_time_other)
    # print(student.remarks)
    messages.success(request,'Update information successfully!')
    return HttpResponseRedirect('/index')
  else:
    user = MyUser.objects.filter(id=id)[0]
    student = user.get_user()
    if student:
      remarks = student.get_single('remarks')
      subjects = student.get_single('subjects')
      subjects_other = student.get_single('subjects_other')
      return render(request,'signup_student.html',{'id':id,'student':student,\
        'remarks':remarks,'subjects':subjects,'subjects_other':subjects_other})
    return render(request, 'signup_student.html',{'id':id})
