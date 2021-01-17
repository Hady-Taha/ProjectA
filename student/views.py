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
    context = {
        'title':'registration',
        'form':form,
    }
    return render(request, 'student/student.html', context)


<<<<<<< HEAD
def attendance(request):
    data_image = request.POST.get('image')
    print(data_image)
=======
def attendance(request):   
>>>>>>> b16c32222c3548ab6a66ef8935f3d1eac326edfe
    context = {
        'title': 'attendance',
    }
    return render(request, 'student/attendance.html',context)
