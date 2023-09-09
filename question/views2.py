from django.views import generic
from .models import Question

class Questionlist(generic.ListView):
    model = Question
    