from django.urls import path
from .views import ArtistaListView, ArtistaDetailView

urlpatterns = [
    path('artistas/', ArtistaListView.as_view()),
    path('artistas/<int:pk>/', ArtistaDetailView.as_view()),
]