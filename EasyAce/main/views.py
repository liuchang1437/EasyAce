from django.shortcuts import render
from myAuth.models import Tutor,MyUser,Student
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
    except DoseNotExist as e:
        pass
    if user.role=='tutor':
        tutor = user.get_user()
        return render(request, 'information_tutor.html', {'tutor':tutor})
    elif user.role=='student':
        student = user.get_user()
        return render(request, 'information_student.html', {'student':student})
    else:
        return render(request, 'index.html')
def view_tutor(request):
    param1 = request.GET.get('p1')
    param2 = request.GET.get('p2')
    if param1 or param2:
        pass
    else:
        tutors = Tutor.objects.all()
    return render(request, 'view_tutor.html', {'tutors':tutors})