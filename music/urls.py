from django.urls import path
from .views import ArtistaListView, ArtistaDetailView, AlbumListView, AlbumDetailView,UserLoginView,CancionDetailView,CancionListView,ListaListView,ListaDetailView,CancionReproduccionView
urlpatterns = [
    path('login/', UserLoginView.as_view()),
    path('artistas/', ArtistaListView.as_view()),
    path('artistas/<int:pk>/', ArtistaDetailView.as_view()),
    path('albumes/', AlbumListView.as_view()),
    path('albumes/<int:pk>/', AlbumDetailView.as_view()),
    path('canciones/', CancionListView.as_view()),
    path('canciones/<int:pk>/', CancionDetailView.as_view()),
    path('listas/', ListaListView.as_view()),
    path('listas/<int:pk>/', ListaDetailView.as_view()),
    path('canciones/<int:pk>/reproducciones/', CancionReproduccionView.as_view())
    
]