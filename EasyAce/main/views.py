from django.shortcuts import render
from myAuth.models import Tutor
# Create your views here.

def index(request):
    return render(request, 'index.html')
def view_tutor(request):
    param1 = request.GET.get('p1')
    param2 = request.GET.get('p2')
    if param1 or param2:
        pass
    else:
        tutors = Tutor.objects.all()
    return render(request, 'view_tutor.html', {'tutors':tutors})