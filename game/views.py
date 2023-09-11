from django.shortcuts import render, get_object_or_404
from .models import Profile, Question, Answer
from django.http import HttpResponse


# Create your views here.


def login_page(request):
    return render(request, 'game/login_page.html')


def game(request):
    # all_questions = Question.objects.all().values()
    # all_answers = Answer.objects.all().values()
    current_question_with_answer = []

    for data_question, data_answer in zip(Question.objects.all().values(), Answer.objects.all().values()):
        current_question_with_answer.extend([{'user': Profile.objects.get(id=request.user.id),
                                          'points': Profile.objects.get(id=request.user.id).points,
                                          'question': data_question['question'],
                                          'array_of_answers': data_answer['array_of_answers'],
                                          'correct_answer': data_answer['correct_answer']}])
    print(current_question_with_answer)

    return render(request, "game/game.html", {'current_question_with_answer': current_question_with_answer})
