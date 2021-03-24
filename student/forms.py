from django import forms
from .models import StudentProfile



class AddNewStudent(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('firstName', 'lastName','studentId','level','department','gender',)




    def clean(self):
        cd = self.cleaned_data
        if StudentProfile.objects.filter(studentId=cd['studentId']).exists():
            raise forms.ValidationError('User exists')
