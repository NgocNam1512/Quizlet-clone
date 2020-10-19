from rest_framework import serializers
from app.models import Flashcard, Card

class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ['id', 'title']