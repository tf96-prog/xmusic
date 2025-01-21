from django.urls import path
from music import views

urlpatterns = [
    path('music/', views.artista_list),
    path('music/<int:pk>/', views.artista_detail),
]