from django.urls import path
from .views import ArtistaListView, ArtistaDetailView, AlbumListView, AlbumDetailView,UserLoginView,CancionDetailView,CancionListView
urlpatterns = [
    path('login/', UserLoginView.as_view()),
    path('artistas/', ArtistaListView.as_view()),
    path('artistas/<int:pk>/', ArtistaDetailView.as_view()),
    path('albumes/', AlbumListView.as_view()),
    path('albumes/<int:pk>/', AlbumDetailView.as_view()),
    path('canciones/', CancionListView.as_view()),
    path('canciones/<int:pk>/', CancionDetailView.as_view()),
]