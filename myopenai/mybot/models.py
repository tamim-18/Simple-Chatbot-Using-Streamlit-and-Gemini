# chatbot/models.py
from django.db import models

class Prompt(models.Model):
    prompt = models.TextField()

    def __str__(self):
        return self.prompt
