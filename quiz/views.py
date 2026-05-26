from django.shortcuts import render
from .models import Quiz, Question, Answer

# Create your views here.

def index(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/index.html', {'quizzes': quizzes})

def view_detail(request, id):
    quiz = Quiz.objects.get(id=id)
    questions = Question.objects.filter(quiz=quiz)
    return render(request, 'quiz/detail.html', {'quiz': quiz, 'questions': questions})

def submit_quiz(request, id):
    if request.method == 'POST':
        quiz = Quiz.objects.get(id=id)
        questions = Question.objects.filter(quiz=quiz)
        score = 0
        total = questions.count()
        
        for question in questions:
            selected_answer_id = request.POST.get(f'question_{question.id}')
            if selected_answer_id:
                answer = Answer.objects.get(id=selected_answer_id)
                if answer.is_correct:
                    score += 1
        
        return render(request, 'quiz/result.html', {
            'score': score,
            'total': total,
            'quiz': quiz
        })