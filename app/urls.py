from django.urls import path, include
from app import views

urlpatterns = [
    path('flashcards/', views.FlashcardList.as_view()),
    path('flashcards/<int:pk>', views.FlashcardDetail.as_view()),
    path('cards/', views.CardList.as_view()),
    path('cards/<int:pk>', views.CardDetail.as_view()),
]

# url for login Browsable API
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
