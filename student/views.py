from django.shortcuts import render
from .forms import AddNewStudent
import base64
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


def attendance(request):
    if request.method=='POST':
        img_data=request.POST['data']
        x=img_data.replace('data:image/png;base64,','')
        name_binary = f'{x}'.encode('utf-8')

        import base64
        with open("media/imageToSave5.png", "wb") as fh:
            fh.write(base64.decodebytes(name_binary))
         
     
    context = {
        'title': 'attendance',
    }
    return render(request, 'student/attendance.html',context)
