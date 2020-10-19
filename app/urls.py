from django.urls import path
from app import views

urlpatterns = [
    path('flashcards/', views.FlashcardList.as_view()),
    path('flashcards/<int:pk>', views.FlashcardDetail.as_view()),
]
