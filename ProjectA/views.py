from django.shortcuts import render


def welcome(request):
    context={}
    return render(request, 'main/welcome.html', context)
