from django.shortcuts import render

def teknisk(request):
    return render(request, 'teknisk/teknisk.html', context=None)
