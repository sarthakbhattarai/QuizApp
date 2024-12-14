# quiz/models.py
from django.db import models
from django.contrib.auth.models import User

class QuizType(models.Model):
    name = models.CharField(max_length=255)
    duration = models.PositiveIntegerField(null=True,help_text="Duration in minutes")

    def __str__(self):
        return self.name

class Question(models.Model):
    quiz_type = models.ForeignKey(QuizType, related_name='questions', on_delete=models.CASCADE,null=True)
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class PlayerPerformance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz_type = models.ForeignKey(QuizType, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz_type.name} - {self.score}"
