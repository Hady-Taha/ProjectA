from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth import authenticate , login, logout
from .forms import NewUserForm,LoginUserForm

# Create your views here.
def register(request):
    form=NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            newuser = form.save(commit=False)
            newuser.set_password(request.POST['password'])
            newuser.save()
            username=request.POST['username']
            password=request.POST['password']
            vLogin(request, username, password)
            return redirect('/')
    
    context = {
        'title':'register',
        'form': form,
        }
    return render(request,'profiles/register.html',context)



def vLogin(request, username=None, password=None):
    if request.user.is_authenticated:
        return redirect('/')
    form = LoginUserForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
            

    context = {
    'title': 'Login',
    'form':form,
    }
    return render(request, 'profiles/login.html', context)


def vLogout(request):
    if request.user.is_authenticated == False:
        return redirect('login')
    logout(request)
    context = {
    'title': 'Logout',
    }
    return redirect('login')
