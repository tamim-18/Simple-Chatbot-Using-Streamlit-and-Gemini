# chatbot/views.py
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Prompt
from .serializers import PromptSerializer
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

class ChatbotView(CreateAPIView):
    serializer_class = PromptSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            prompt = serializer.validated_data['prompt']

            # Generate response from Gemini
            try:
                response = model.generate_content(prompt)
                chatbot_response = response.text
                return Response({'response': chatbot_response}, status=status.HTTP_200_OK)
            except Exception as e:
                # Handle any errors that occur during API call
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
