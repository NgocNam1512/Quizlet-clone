from rest_framework import serializers
from app.models import Flashcard, Card

class FlashcardSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    class Meta:
        model = Flashcard
        fields = ['id', 'title', 'is_private', 'author']

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'vocabulary', 'meaning', 'flashcard']