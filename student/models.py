from django.db import models


# Create your models here.
class StudentProfile(models.Model):

    STUDENTGENDER = [('male', 'male'), ('female', 'female')]
    LEVEL = [('level 1','level 1'),('level 2','level 2'),('level 3','level 3'),('level 4','level 4')]
    DEPARTMEMT = [('Cs','Cs'),('It','It'),('General','General')]


    firstName=models.CharField(max_length=150,blank=True, null=True)
    lastName=models.CharField(max_length=150,blank=True, null=True)
    studentId=models.IntegerField(blank=True, null=True)
    level=models.CharField(max_length=30, blank=True , null=True,choices=LEVEL)
    department= models.CharField(max_length=30,blank=True, null=True,choices=DEPARTMEMT)
    gender = models.CharField(max_length=20, blank=True, null=True, choices=STUDENTGENDER)
    image = models.ImageField(upload_to='studentImages', default='studentImages/user.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class StudentAttendence(models.Model):
<<<<<<< HEAD
    
=======
    time=models.DateTimeField()
>>>>>>> b16c32222c3548ab6a66ef8935f3d1eac326edfe
    studentId=models.IntegerField(blank=True, null=True)
    firstName=models.CharField(max_length=150,blank=True, null=True)
    level=models.CharField(max_length=30, blank=True , null=True)
    department= models.CharField(max_length=30,blank=True, null=True)
<<<<<<< HEAD
    time=models.DateTimeField(auto_now=True)
=======
>>>>>>> b16c32222c3548ab6a66ef8935f3d1eac326edfe
