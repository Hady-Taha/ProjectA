from django.contrib import admin
from .models import StudentProfile,StudentAttendence
# Register your models here.

admin.site.register(StudentProfile)
admin.site.register(StudentAttendence)