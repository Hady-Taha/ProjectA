from django.shortcuts import render


def welcome(request):
    context = {
        'title':'welcome',
    }
    return render(request, 'main/welcome.html', context)
