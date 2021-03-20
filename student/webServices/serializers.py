from rest_framework import serializers
from student.models import StudentProfile , StudentAttendence






class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentProfile
        fields = '__all__'


class StudentAttendenceSerilalizer(serializers.ModelSerializer):
    class Meta:
        model=StudentAttendence
        fields = '__all__'
      