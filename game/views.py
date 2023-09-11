from django.shortcuts import render, get_object_or_404
from .models import Profile, Question, Answer

# Create your views here.


def login_page(request):
    return render(request, "game/login_page.html")


def game(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answer = Answer.objects.get(question_id=request.user.id)
    user = Profile.objects.get(id=request.user.id)

    print(question.id)

    data = {
        "user": user,
        "points": user.points,
        "question_id": question.id,
        "question": question.question,
        "array_of_answers": answer.array_of_answers,
        "correct_answer": answer.correct_answer,
    }

    next_page = question.id + 1

    return render(
        request,
        "game/game.html",
        {"data": data, "pk": next_page},
    )

