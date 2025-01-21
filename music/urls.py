from django.urls import path
from music import views

urlpatterns = [
    path('artistas/', views.artista_list),
    path('artistas/<int:pk>/', views.artista_detail),
]