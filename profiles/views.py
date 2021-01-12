from django.shortcuts import render

# Create your views here.
def register(request):
    context = {
        'title':'register',
    }
    return render(request,'profiles/register.html',context)