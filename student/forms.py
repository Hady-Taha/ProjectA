from django import forms
from .models import StudentProfile



class AddNewStudent(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = '__all__'




def clean(self):
    cd = self.cleaned_data
    if StudentProfile.objects.filter(studentId=cd['studentId']).exists():
         raise forms.ValidationError('User exists')
