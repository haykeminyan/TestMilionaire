from django.shortcuts import render, get_object_or_404
from .models import Profile, Question, Answer


def game(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answer = Answer.objects.get(question_id=request.user.id)
    user = Profile.objects.get(id=request.user.id)

    data = {
        "user": user,
        "points": user.points,
        "question_id": question.id,
        "question": question.question,
        "array_of_answers": answer.array_of_answers,
        "correct_answer": answer.correct_answer,
    }

    next_page = question.id + 1
    print(request.user)
    # if request.method == "POST":
    variant = request.POST.get("variant", 0)
    if variant == answer.correct_answer:
        user.points += 1
    else:
        user.points += 0
        print('NO')
    # print(data)
    # print( user.points)
    return render(
        request,
        "game/game.html",
        {"data": data, "pk": next_page, "variant": variant},
    )

