# # chatbot/models.py
# from django.db import models

# class Prompt(models.Model):
#     prompt = models.TextField()

#     def __str__(self):
#         return self.prompt
# chatbot/models.py
from django.db import models


class Prompt(models.Model):
    prompt = models.TextField()
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    response_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.prompt


class User(models.Model):
   
    username = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




    
    def __str__(self):
        return self.username
