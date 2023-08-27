from django.shortcuts import render
from .models import Question


def question_list(request):
    data = Question.objects.all()
    return render(request,'all_question.html',{'question':data})
    
    
    
    
    
    
def question_detail(request,question_id):
    data = Question.objects.get(id=question_id)
    return render(request,'question_detail.html',{'question':data})