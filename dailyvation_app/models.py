from django.contrib.auth.models import User
from django.db import models


class MotivationalPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=300)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} by {self.author.username}'
