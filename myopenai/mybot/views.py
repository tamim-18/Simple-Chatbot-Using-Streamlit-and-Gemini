# # chatbot/views.py
# from rest_framework.generics import CreateAPIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Prompt
# from .serializers import PromptSerializer
# import google.generativeai as genai
# import os
# from dotenv import load_dotenv

# load_dotenv()
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# model = genai.GenerativeModel('gemini-pro')

# class ChatbotView(CreateAPIView):
#     serializer_class = PromptSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             prompt = serializer.validated_data['prompt']

#             # Generate response from Gemini
#             try:
#                 response = model.generate_content(prompt)
#                 chatbot_response = response.text
#                 return Response({'response': chatbot_response}, status=status.HTTP_200_OK)
#             except Exception as e:
#                 # Handle any errors that occur during API call
#                 return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# chatbot/views.py
# chatbot/views.py
# chatbot/views.py
# chatbot/views.py
# chatbot/views.py
# from rest_framework.generics import CreateAPIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Prompt
# from .serializers import PromptSerializer
# import os
# from dotenv import load_dotenv
# from openai import OpenAI
# from rest_framework.exceptions import ValidationError

# load_dotenv()

# # Create an OpenAI client instance with the API key
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



# class ChatbotView(CreateAPIView):
#     serializer_class = PromptSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             prompt = serializer.validated_data['prompt']

#             # Generate response from OpenAI GPT-4
#             try:
#                 response = client.completions.create(
#                     model="gpt-3.5-turbo",  # Use "davinci-codex" engine for GPT-4
#                     prompt=prompt,
#                     max_tokens=150,  # Adjust the response length as needed
#                      # Specify the GPT model to use
#                 )
#                 chatbot_response = response['choices'][0]['text'].strip()
#                 return Response({'response': chatbot_response}, status=status.HTTP_200_OK)
#             except Exception as e:
#                 # Handle any errors
#                 return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         else:
#             # Return validation errors if serializer is not valid
#             raise ValidationError(serializer.errors)
# chatbot/views.py
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Prompt
from .serializers import PromptSerializer
import google.generativeai as genai
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')


class ChatbotView(CreateAPIView):
    serializer_class = PromptSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            prompt_text = serializer.validated_data['prompt']

            # Generate response from Gemini
            try:
                response = model.generate_content(prompt_text)
                chatbot_response = response.text

                # Save prompt and response to database
                prompt = Prompt.objects.create(prompt=prompt_text, response=chatbot_response,
                                               created_at=datetime.now(), response_time=datetime.now())

                # Serialize prompt for response
                prompt_serializer = PromptSerializer(prompt)
                return Response(prompt_serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                # Handle any errors that occur during API call
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
