from django.views import generic
from .models import Question


# contexst: question_list or object_list Because we have many questions
class Questionlist(generic.ListView):
    model = Question
