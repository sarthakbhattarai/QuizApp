from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_view, name='quiz_home'),
    path('start/<int:quiz_id>/', views.start_quiz, name='start_quiz'),
    path('question/', views.question_detail_view, name='question_detail'),
]
