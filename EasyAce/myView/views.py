from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def for_student(request):
    return render(request, 'for_student.html')

def information_tutor(request):
    return render(request, 'information_tutor.html')

def match_tutor(request):
    return render(request, 'match_tutor.html')

def search_tutor(request):
    return render(request, 'search_tutor.html')