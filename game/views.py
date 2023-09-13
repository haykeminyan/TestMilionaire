from django.shortcuts import get_object_or_404, render

from .models import Answer, Profile, Question


def game(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answer = Answer.objects.get(question_id=pk)
    user = Profile.objects.get(id=request.user.id)

    data = {
        'user': user,
        'points': user.points,
        'question_id': question.id,
        'question': question.question,
        'array_of_answers': answer.array_of_answers,
        'correct_answer': answer.correct_answer,
    }

    next_page = question.id + 1

    variant = request.POST.get('variant', None)

    if variant:
        if variant == answer.correct_answer:
            if question.id in range(1, 3):
                user.points += 5
            elif question.id in range(3, 5):
                user.points += 10
            elif question.id in range(5, 7):
                user.points += 20
            Profile.objects.filter(id=request.user.id).update(points=user.points)

    return render(
        request,
        'game/game.html',
        {
            'data': data,
            'pk': next_page,
            'points': user.points,
            'variant': variant,
            'answer': answer.correct_answer,
        },
    )


def result(request):
    user = Profile.objects.get(id=request.user.id)
    return render(request, 'result/result.html', {'user': user})
