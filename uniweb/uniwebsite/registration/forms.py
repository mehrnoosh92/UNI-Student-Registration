from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        #fields = ['name' , 'family']
        #vali ma in raho nemirim shayad
        #fieldha ziad bashe , all behtare