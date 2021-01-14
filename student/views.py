from django.shortcuts import render
from .forms import AddNewStudent
# Create your views here.

def student(request):
    form=AddNewStudent()
    context = {
        'title':'registration',
        'form':form,
    }
    return render(request, 'student/student.html', context)