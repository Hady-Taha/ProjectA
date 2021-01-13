from django.shortcuts import render


def home(request):
    context = {
<<<<<<< HEAD
        'title':'home',
=======
        'title':'Home',
>>>>>>> 53798d577ac304b1dabf58efb528e00c84df5961
    }
    return render(request, 'main/home.html', context)
