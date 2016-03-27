from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    author = models.ForeignKey('django.contrib.auth.User')
    likes = models.ManyToMany('django.contrib.auth.User')
    
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey('Question')
    author = models.ForeignKey('django.contrib.auth.User')