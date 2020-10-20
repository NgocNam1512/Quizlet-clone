from app.models import Flashcard, Card
from app.serializers import FlashcardSerializer, CardSerializer
from app.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions, filters

class FlashcardList(generics.ListCreateAPIView):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class FlashcardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

# class FlashcardSearch(generics.ListAPIView):
#     queryset = Flashcard.objects.all()
#     serializer_class = FlashcardSerializer
