from django import forms
from .models import StudentProfile
class AddNewStudent(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields=('__all__',)
    pass
