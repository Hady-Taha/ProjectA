from django import forms

from django.contrib.auth.models import User





class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=('username','password','password2','email')
    
    # password = forms.CharField(widget=forms.PasswordInput())
    # password2 = forms.CharField(label='confirm Password', widget=forms.PasswordInput())

    username=forms.CharField(
        max_length=25,
        min_length=3,
        required=True,
        widget=forms.TextInput(
            attrs={'id':'name','placeholder':'Your Name'}
            )
    )

    
    password=forms.CharField(
        min_length=9,
        required=True,
        widget=forms.PasswordInput(
            attrs={'id':'form-pass','placeholder':'Password'}
            
            )
    )

    password2=forms.CharField(
        min_length=9,
        required=True,
        widget=forms.PasswordInput(
            attrs={'id':'re_pass','placeholder':'Repeat your password'}
            
            )
    )



    email=forms.EmailField(
        min_length=7,
        required=True,
        widget=forms.EmailInput(
            attrs={'id':'email','placeholder':'Your Email'}
        )

    )



    
    def clean(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('User exists')
        
        
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('password not match')
        




class LoginUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=('username','password',)
    

    username=forms.CharField(
        min_length=3,
        required=True,
        widget=forms.TextInput(
            attrs={'id':'your_name','placeholder':'Your Name'}
        )

    )
    password=forms.CharField(
        min_length=9,
        required=True,
        widget=forms.PasswordInput(
            attrs={'id':'your_pass','placeholder':'Password'}
        )

    )


