from django.shortcuts import render, get_object_or_404
from .models import Profile, Question, Answer
from django.http import HttpResponse
# Create your views here.


def login(request):
    return render(request, "login/login.html")


def game(request):
    question = Question.objects.all().values()
    answer = Answer.objects.all().values()
    data = {'question': question, 'answer': answer}
    return render(request, "game/game.html", {'data': data})

