from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cat

cat = None


def home(request):
    return render(request, 'home.html')


def create_cat(request):
    global cat
    if request.method == 'POST':
        name = request.POST['name']
        cat = Cat(name)
        return redirect('cat_stats')
    return render(request, 'home.html')


def cat_stats(request):
    global cat
    if not cat:
        return redirect('home')

    if request.method == 'POST':
        action = request.POST['action']
        if action == 'feed':
            cat.feed()
        elif action == 'play':
            cat.play()
        elif action == 'sleep':
            cat.sleep()

    context = {
        'cat': cat
    }
    return render(request, 'cat_stats.html', context)
