from django.shortcuts import render
from .forms import NewUserForm

# Create your views here.
def register(request):
    form=NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            newuser = form.save(commit=False)
            newuser.set_password(request.POST['password'])
            newuser.save()
    context = {
        'title':'register',
        'form':form,
    }
    return render(request,'profiles/register.html',context)
