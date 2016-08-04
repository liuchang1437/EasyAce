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
from EasyAce.settings import SECRET_KEY
from django.core.mail import send_mail
from .utils import Token

token_confirm = Token(SECRET_KEY)

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
        messages.error(request,'The account has been disabled!')
        return HttpResponseRedirect('myAuth:login')
    else:
      messages.error(request,'The username and password were incorect.')
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
        tutor = Tutor()
        tutor.base_info = user
        tutor.name = username
        tutor.save()
        return HttpResponseRedirect(reverse('myAuth:signup_tutor'))
      else:
        student = Student()
        student.base_info = user
        student.name = student.username
        student.save()
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
    tutor = myuser.get_user()
    tutor.username = myuser.username
    tutor.name=name
    tutor.gender=gender
    tutor.phone=phone
    tutor.birth=birth
    tutor.school=school
    tutor.wechat=wechat
    tutor.whatsapp=whatsapp
    tutor.email=email
    tutor.teach_duration=teach_duration
    tutor.num_taught=num_taught
    tutor.achievement=achievement
    tutor.base_info=myuser
    
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
    tutor.save()
    messages.success(request,'Update information successfully!')
    return HttpResponseRedirect('/index')
  else:
    return render(request, 'signup_tutor.html')




@login_required
def signup_student(request):
  if request.method == 'POST':
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
    student = myuser.get_user()
    student.username=myuser.username
    student.name=name
    student.gender=gender
    student.email=email
    student.phone=phone
    student.school=school
    student.grade=grade
    student.wechat=wechat
    student.whatsapp=whatsapp
    student.base_info=myuser
    student.location=location
    student.loc_nego=loc_nego
    student.time_per_lesson=time_per_lesson
    student.start_time=start_time
    student.lesson_per_week=lesson_per_week
    student.prefer_tutor_gender=prefer_tutor_gender
    if start_time=='Other':
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
    #### Create student end

    #### Start create prefer teach and refer teach
    student_subject = request.POST['student_subject'] 
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
    return HttpResponseRedirect('/index')
  else:
    return render(request, 'signup_student.html')

@login_required
def change_password(request):
  if request.method=='POST':
    new_password = request.POST['password']
    request.user.set_password(new_password)
    request.user.save()
    messages.success(request,'Change password successfully!')
    return HttpResponseRedirect('/index')
  return render(request, 'chage_password.html')
def forget_password(request):
  if request.method == 'POST':
    email = request.POST['email']
    try:
      user = MyUser.objects.get(email=email)
      username = user.username
    except:
      messages.error(request,'The email does not exists!')
      return HttpResponseRedirect(reverse('myAuth:forget_password'))
    token = token_confirm.generate_validate_token(username)
    ## send mail
    message = '\n'.join(
      [
        'hi, {}, please click the link below to change your password.'.format(username),
        '/'.join([request.get_host(),'auth/validate',token])
      ]
    )
    send_mail('Change your password',message,None,[email],fail_silently=False)
    messages.success(request,'An email has been send to {}, please check it in 2 hours.'.format(email))
    return HttpResponseRedirect('/index')
  return render(request,'forget_password.html')
def validate_email(request,token):
  if request.method == 'POST':
    try:
      username = token_confirm.confirm_validate_token(token)
    except:
      messages.error(request,'The link has been expired.')
      return HttpResponseRedirect('/index')
    try:
      user = MyUser.objects.get(username=username)
    except User.DoesNotExist:
      messages.error(request,'The user does not exists!')
      return HttpResponseRedirect('/index')
    user.set_password(request.POST['new_password'])
    user.save()
    messages.success(request,'Change password successfully!')
    return HttpResponseRedirect('/index')
  return render(request,'change_password.html',{'token':token})