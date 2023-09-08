from django.shortcuts import render, get_object_or_404
from .models import Profile
from django.http import HttpResponse
# Create your views here.


def greeting(request):
    current_user = get_object_or_404(Profile, id=request.user.id)
    context = {"current_user": current_user}
    return render(request, "greeting/greeting.html", context)

def game(request):
    xyi = {'xyi': 'xyi'}
    return render(request, "game/game.html", xyi)
