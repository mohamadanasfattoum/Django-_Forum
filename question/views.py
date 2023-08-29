from django.shortcuts import render , redirect
from .models import Question
from .forms import QuestionForm

def question_list(request):
    data = Question.objects.all()
    return render(request,'all_question.html',{'question':data})
    
    
    
    
    
    
def question_detail(request,question_id):
    data = Question.objects.get(id=question_id)
    return render(request,'question_detail.html',{'question':data})


def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(f'/question/')

    else:
        form = QuestionForm()

    return render(request,'add_question.html',{'form':form})