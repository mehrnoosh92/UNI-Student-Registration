from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def student_show_view(request):
    student = Student.objects.all()
    return render(request, 'student_show.html', {'student':student})
    