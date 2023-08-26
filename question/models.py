from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    user = models.ForeignKey(User,related_name='post_auther',on_delete=models.SET_NULL,null=True)