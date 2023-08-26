from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Question(models.Model):
    user = models.ForeignKey(User,related_name='Quetion_user',on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=5000)
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self) -> str:
        return self.title
    
class Answer(models.Model):
    user = models.ForeignKey(User,related_name='Quetion_answer',on_delete=models.CASCADE)
    question = models.ForeignKey(Question,related_name='answer_question', on_delete=models.CASCADE)
    answer = models.TextField(max_length=5000)
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self) -> str:
        return str(self.question)