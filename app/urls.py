from django.urls import path, re_path
from app import views

urlpatterns = [
    # The home page
    re_path(r'^.*\.html', views.pages, name='pages'),
    path('', views.index, name='home'),
]
