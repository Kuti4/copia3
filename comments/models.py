from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Comment(models.Model):
    text = models.CharField(max_length=512)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __init__(self, user, text) -> None:
        self.text = text
        self.date = datetime.now()
        self.user = user