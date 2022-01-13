from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.


class Polls(models.Model):
    name = models.TextField(null=True)
    start_time = models.DateTimeField(default=now, editable=False)
    end_time = models.DateTimeField(null=True)
    description = models.TextField(null=True)


class Questions(models.Model):
    poll = ForeignKey(Polls, on_delete=CASCADE, related_name='questions', null=False)
    QUESTIONS_CHOICES = [
        ('txt', 'Ответ текстом'),
        ('one', 'Ответ с одним вариантом'),
        ('few', 'Ответ с несколькими вариантами'),
    ]
    question_text = models.CharField(max_length=255)
    type = models.CharField(max_length=3, choices=QUESTIONS_CHOICES)


class Answers(models.Model):
    user_id = IntegerField(null=False)
    poll = ForeignKey(Polls, on_delete=CASCADE, related_name='answers', null=False)
    question = ForeignKey(Questions, on_delete=CASCADE, null=False)
    answer = models.TextField(null=False)
