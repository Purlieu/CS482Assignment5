from django.db import models
from django import forms
# Create your models here.

class State(models.Model):
    state_name = models.CharField(max_length=120, default="")
    title = models.CharField(max_length=120)
    text = models.CharField(max_length = 2048)
    options = models.CharField(max_length=120)

class Option(models.Model):
    text = models.CharField(max_length=120)
    current_state = models.ForeignKey(State, related_name='current_state', on_delete=models.CASCADE)
    next_state = models.ForeignKey(State, related_name='next_state', on_delete=models.CASCADE)

class StateMachine(models.Model):
    user_state = models.ForeignKey(State, related_name="user_state", on_delete=models.CASCADE)
