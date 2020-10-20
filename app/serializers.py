from rest_framework import serializers
from app.models import Flashcard, Card

class FlashcardSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    cards = serializers.PrimaryKeyRelatedField(many=True, queryset=Card.objects.all())
    class Meta:
        model = Flashcard
        fields = ['id', 'title', 'is_private', 'author', 'cards']

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'vocabulary', 'meaning', 'flashcard']