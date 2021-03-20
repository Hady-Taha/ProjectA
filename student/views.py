from django.shortcuts import render , redirect
from .forms import AddNewStudent
from .models import StudentProfile,StudentAttendence
import base64
import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt
from .IPCode import iris
# Create your views here.



def student(request):
    if request.user.is_authenticated==False:
        return redirect('login')
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
    if request.user.is_authenticated==False:
        return redirect('login')
    if request.method=='POST':
        img_data=request.POST['data']
        x=img_data.replace('data:image/png;base64,','')
        name_binary = f'{x}'.encode('utf-8')
        # print(x)
        with open("media/imageToSave5.png", "wb") as fh:
            fh.write(base64.decodebytes(name_binary))
        image=StudentProfile.objects.values('image')

        for i in image:
            x=str(i.get('image'))
            imgToDB = cv2.imread('media/'+x)
            eyeToDB = iris(imgToDB)
            kpToDB = eyeToDB.toKP()

            # iris from front-end to test
            imgNew = cv2.imread("media/imageToSave5.png")
            eyeNew = iris(imgNew)
            student=StudentProfile.objects.get(image=x)
            x=eyeNew.match(kpToDB)
            print(x)
            if x>=15:
                StudentAttendence.objects.get_or_create(student=student)
    attendence=StudentAttendence.objects.all()
    context = {
        'title': 'attendance',
        'attendence': attendence,
        
    }
    return render(request, 'student/attendance.html',context)
