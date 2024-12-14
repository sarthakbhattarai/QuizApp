from django.contrib import admin
from .models import QuizType, Question, Choice, PlayerPerformance

@admin.register(QuizType)
class QuizTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz_type', 'created_at')

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')

@admin.register(PlayerPerformance)
class PlayerPerformanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz_type', 'score', 'completed_at')