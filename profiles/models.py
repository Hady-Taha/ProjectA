from django.db import models



STUDENTGENDER = [('male','male'),('female','female')]
# Create your models here.
class StudentProfile(models.Model):
        firstName=models.CharField(max_length=150,blank=True, null=True)
        lastName=models.CharField(max_length=150,blank=True, null=True)
        studentId=models.IntegerField(blank=True, null=True)
        level=models.CharField(max_length=30, blank=True , null=True)
        department= models.CharField(max_length=30,blank=True, null=True)
        gender = models.CharField(max_length=20,)
        image = models.ImageField(upload_to='studentImages', default='studentImages/user.png')
        created = models.DateTimeField(auto_now_add=True)
        ver = models.BooleanField(default=False)




    """
    TODO
    1- import model User from auth model .
    2- add fields .
    3- add functions .
    4- add what you need
    """

    pass