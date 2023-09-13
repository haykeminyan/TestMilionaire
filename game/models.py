from django.db import models
import json
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name_plural = "1. Profile"


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=250)
    date_created_question = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.question}"

    class Meta:
        verbose_name_plural = "2. Question"


class Answer(models.Model):
    question = models.OneToOneField(
        Question,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    array_of_answers = models.JSONField(default=list)
    correct_answer = models.CharField(max_length=30)

    def __str__(self):
        return (f"Correct answer to the question"
                f" \"{self.question}\" is {self.correct_answer}")

    class Meta:
        verbose_name_plural = "3. Answer"
