from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import LoginForm,SignupForm
from .models import MyUser
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
      user = Myuser.objects.create_user(username=username,role=role,password=password)
      user.save()
      if role=='TU':
        return HttpResponseRedirect(reverse('myAuth:signup_tutor',kwargs={'id':user.id}))
      elif role=='ST':
        return HttpResponseRedirect(reverse('myAuth:signup_student',kwargs={'id':user.id}))
      return HttpResponseRedirect(reverse('main:index'))
  else:
    return render(request,'signup.html')

def logout(request):
  logout_user(request)
  return HttpResponseRedirect('/index')
def signup_tutor(request,id):
  print(id)
  return render(request, 'signup_tutor.html')
def signup_student(request,id):
  print(id)
  return render(request, 'signup_student.html')
