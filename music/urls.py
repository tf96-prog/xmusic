from django.urls import path
from .views import ArtistaListView, ArtistaDetailView, AlbumListView, AlbumDetailView

urlpatterns = [
    path('artistas/', ArtistaListView.as_view()),
    path('artistas/<int:pk>/', ArtistaDetailView.as_view()),
    path('albumes/', AlbumListView.as_view()),
    path('albumes/<int:pk>/', AlbumDetailView.as_view()),
]