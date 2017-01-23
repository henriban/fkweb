from django.shortcuts import render

# Create your views here.


def navbar(request):
    return render(request, 'mainpage/navbar.html', context=None)


def slideshow(request):
    return render(request, 'mainpage/slideshow.html', context=None)
