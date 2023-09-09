from django.views import generic
from .models import Question


# contexst: question_list or object_list Because we have many questions
class Questionlist(generic.ListView):
    model = Question


class QuestionDetail(generic.DetailView):
    model = Question



class QuestionCreate(generic.CreateView):
    model = Question
    fields='__all__'
    success_url= '/question/'



class QuestionUpdate(generic.UpdateView):
    model = Question
    fields='__all__'
    success_url= '/question/'
    template_name= 'question/edit_question.html'


class QuestionDelete(generic.DeleteView):
    pass