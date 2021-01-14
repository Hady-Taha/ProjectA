from django.shortcuts import render
from .forms import AddNewStudent
# Create your views here.

def student(request):
    form = AddNewStudent()
    if request.method == 'POST':
        form = AddNewStudent(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            pass
        pass
    context = {
        'title':'registration',
        'form':form,
    }
    return render(request, 'student/student.html', context)
