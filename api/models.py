from django.db import models

# Create your models here.

class Question(models.Model):
    roomname = models.CharField(max_length=200, blank=False, default="no room")
    question = models.TextField(max_length=200, blank=False)
    option1 = models.CharField(max_length=200, blank=False)
    option2 = models.CharField(max_length=200, blank=False)
    option3 = models.CharField(max_length=200, blank=False)
    option4 = models.CharField(max_length=200, blank=False)
    answer = models.IntegerField()
    qid = models.CharField(max_length=200)
    def __str__(self):
        return self.question
