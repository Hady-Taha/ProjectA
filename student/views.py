from django.shortcuts import render

# Create your views here.

def student(request):
    context = {
        'title':'registeration',
    }
    return render(request, 'student/student.html', context)