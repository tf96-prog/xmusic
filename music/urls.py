from django.urls import path
from .views import ArtistaViewSet, AlbumViewSet,UserLoginView,CancionViewSet,ListaViewSet,UsuarioView

from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'artistas',ArtistaViewSet,basename='artista')
router.register(r'albumes',AlbumViewSet,basename='album')
router.register(r'canciones',CancionViewSet,basename='cancion')
router.register(r'listas',ListaViewSet,basename='lista')

urlpatterns=router.urls

urlpatterns.append(path('login/', UserLoginView.as_view()))
urlpatterns.append(path('usuarios/yo/', UsuarioView.as_view()))