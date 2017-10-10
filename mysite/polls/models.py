from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200, default="")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f"{self.question_text}"

class Choice(models.Model):
    pass