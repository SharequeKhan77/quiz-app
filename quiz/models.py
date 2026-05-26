from django.db import models

# Create your models here.

class Quiz(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    created_date = models.DateField(auto_now=True)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

class Answer(models.Model):
    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)