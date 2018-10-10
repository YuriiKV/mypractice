from django.shortcuts import render
from .models import Student

def index(request):
    students_list = Student.objects.all()
    return render(request, 'register/index.html', {'students': students_list})
