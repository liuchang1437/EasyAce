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
        return render(request, 'information_student.html', {'student':student,\
            'remarks':remarks,'subjects':subjects})
    else:
        return render(request, 'index.html')

def view_tutor(request):
    regions = request.GET.get('r')
    # = request.GET.get('')
    if regions:
        tutor = Tutor.objects.filter(regions_contains=regions)
    else:
        tutors = Tutor.objects.all()
    return render(request, 'view_tutor.html', {'tutors':tutors})

def edit(request):
    user = request.user
    if user.role=='tutor':
        return HttpResponseRedirect(reverse('myAuth:signup_tutor',kwargs={'id':user.id}))
    else:
        return HttpResponseRedirect(reverse('myAuth:signup_student',kwargs={'id':user.id}))