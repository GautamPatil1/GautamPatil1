from django.shortcuts import render
import requests

# Create your views here.


def todo(request):
    return render(request, 'todo.html')


def weather(request):
    return render(request, 'weather.html')


def quiz(request):
    return render(request, 'quiz.html')


def palette(request):
    return render(request, 'palette.html')


def story(request):
    url = 'https://shortstories-api.onrender.com/'
    response = requests.get(url).json()
    return render(request, 'story.html', response)


def index(request):
    return render(request, 'index.html')