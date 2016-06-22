from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import LoginForm,SignupForm
from .models import MyUser
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user


def login(request):
		# if this is a POST request we need to process the form data
		if request.method == 'POST':
				username = request.POST['username']
				password = request.POST['password']
				user = authenticate(username=username, password=password)
				if user is not None:
						if user.is_active:
								login_user(request,user)
								return HttpResponseRedirect('/index/')
						else:
								return HttpResponseRedirect('/auth/login/')
				else:
						return HttpResponseRedirect('/auth/login/')
		# if a GET (or any other method) we'll create a blank form
		else:
				form = LoginForm()
		return render(request, 'login.html', {'form': form})

def signup(request):
		if request.method == 'POST':
				form = SignupForm(request.POST)
				if form.is_valid():
						username = form.cleaned_data['username']
						email = form.cleaned_data['email']
						role = form.cleaned_data['role']
						gender = form.cleaned_data['gender']
						phone = form.cleaned_data['phone']
						password = form.cleaned_data['password']
						user = MyUser.objects.create_user(username=username,email=email,role=role,gender=gender,phone=phone,password=password)
						user.save()
						return HttpResponseRedirect('/auth/login/')
		else:
				form = SignupForm()
		return render(request, 'signup.html', {'form': form})

def logout(request):
		logout_user(request)
		return render(request, 'index.html')
