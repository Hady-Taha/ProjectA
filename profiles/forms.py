from django import forms
from django.contrib.auth.models  import User 

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=('username','password','password2',)
    
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(label='confirm Password', widget=forms.PasswordInput())


    def clean(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('password not match')



class LoginUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=('username','password',)
    
