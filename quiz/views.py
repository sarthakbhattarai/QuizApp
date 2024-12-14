from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils.timezone import now
from .models import QuizType, Question, Choice, PlayerPerformance

def quiz_view(request):
    quiz_types = QuizType.objects.all()
    return render(request, 'quiz/quiz.html', {'quiz_types': quiz_types})


def start_quiz(request, quiz_id):
    quiz_type = get_object_or_404(QuizType, id=quiz_id)
    questions = quiz_type.questions.all()

    
    request.session['quiz_type_id'] = quiz_id
    request.session['current_question_index'] = 0  
    request.session['score'] = 0  
    
    return redirect('question_detail')


def question_detail_view(request):
    quiz_id = request.session.get('quiz_type_id')
    quiz_type = get_object_or_404(QuizType, id=quiz_id)
    question_index = request.session.get('current_question_index', 0)
    questions = quiz_type.questions.all()

   
    if question_index >= len(questions):
        score = request.session.get('score', 0)
        PlayerPerformance.objects.create(
            user=request.user,
            quiz_type=quiz_type,
            score=score
        )
        return render(request, 'quiz/result.html', {'quiz_type': quiz_type, 'score': score})

    
    question = questions[question_index]
    choices = question.choices.all()

    if request.method == "POST":
        selected_choice_id = request.POST.get("choice")
        if selected_choice_id:
            selected_choice = get_object_or_404(Choice, id=selected_choice_id)
            if selected_choice.is_correct:
                request.session['score'] += 1  

        
        request.session['current_question_index'] += 1
        return redirect('question_detail')  

    return render(request, 'quiz/question_detail.html', {
        'question': question,
        'choices': choices
    })
