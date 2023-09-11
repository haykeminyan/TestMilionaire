from django.shortcuts import render, get_object_or_404
from .models import Profile, Question, Answer
from django.http import HttpResponse


# Create your views here.


def login_page(request):
    return render(request, "game/login_page.html")


def game(request, pk):
    question = Question.objects.get(id=pk)
    answer = Answer.objects.get(question_id=request.user.id)

    data = {
        "user": Profile.objects.get(id=request.user.id),
        "points": Profile.objects.get(id=request.user.id).points,
        "question_id": question.id,
        "question": question.question,
        "array_of_answers": answer.array_of_answers,
        "correct_answer": answer.correct_answer,
    }
    print(data)
    return render(
        request,
        "game/game.html",
        {"data": data, "next_page": str(int(pk)+1), "previous_page": str(int(pk)-1)},
    )

