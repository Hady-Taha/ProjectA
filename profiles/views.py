from django.shortcuts import render
from .forms import NewUserForm
# Create your views here.
def register(request):
    form=NewUserForm()
    context = {
        'title':'register',
        'form':form,
    }
    return render(request,'profiles/register.html',context)