from django.urls import path
from .views import ChatbotView

from . import views

urlpatterns = [
    path('chatbot', ChatbotView.as_view(), name='chatbot'),
]