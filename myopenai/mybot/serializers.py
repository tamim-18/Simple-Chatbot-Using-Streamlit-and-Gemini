# # chatbot/serializers.py
# from rest_framework import serializers

# class PromptSerializer(serializers.Serializer):
#     prompt = serializers.CharField(max_length=512)
    
from rest_framework import serializers
from .models import Prompt


from rest_framework import serializers
from .models import Prompt


class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = ['prompt', 'response', 'created_at', 'response_time']
        read_only_fields = ['response', 'created_at', 'response_time']