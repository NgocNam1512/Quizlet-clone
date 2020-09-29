from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Flashcard(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Card(models.Model):
    flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE)
    vocabulary = models.CharField(max_length=50)
    meaning = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)