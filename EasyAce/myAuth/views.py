from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import LoginForm,SignupForm
from .models import MyUser,Tutor
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username,password=password)
    if user is not None:
      if user.is_active:
        login_user(request,user)
        return HttpResponseRedirect('/index')
    return HttpResponseRedirect(reverse('myAuth:login'))
  return render(request,'login.html')

def signup(request):
  if request.method=='POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      role = form.cleaned_data['role']
      password = form.cleaned_data['password']
      user = MyUser.objects.create_user(username=username,role=role,password=password)
      user.save()
      if role=='TU':
        return HttpResponseRedirect(reverse('myAuth:signup_tutor',kwargs={'id':user.id}))
      elif role=='ST':
        return HttpResponseRedirect(reverse('myAuth:signup_student',kwargs={'id':user.id}))
    return HttpResponseRedirect('/index')
  else:
    return render(request,'signup.html')

def logout(request):
  logout_user(request)
  return HttpResponseRedirect('/index')
def signup_tutor(request,id):
  if request.method == 'POST':
    name = request.POST['name']
    gender = request.POST['gender']
    #birth = request.POST['birth']
    email = request.POST['email']
    phone = request.POST['phone']
    school = request.POST['school']
    wechat = request.POST['wechat']
    whatsapp = request.POST['whatsapp']
    duration = request.POST['teach_duration']
    num_taught = request.POST['num_taught']
    #achivement = request.POST['achivement']
    myuser = MyUser.objects.filter(id=id)[0]
    myuser.email = email
    tutor = Tutor(name=name,gender=gender,phone=phone,\
      school=school,wechat=wechat,whatsapp=whatsapp,duration=duration,\
      num_st_taught=num_taught,birth='1990-10-01')
    tutor.base_info = myuser
    tutor.save()
    return HttpResponseRedirect('/index')
  return render(request, 'signup_tutor.html',{'id':id})
def signup_student(request,id):
  print(id)
  return render(request, 'signup_student.html',{'id':id})
