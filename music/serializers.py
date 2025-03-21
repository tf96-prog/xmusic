from rest_framework import serializers
from music.models import Artista,Album,Cancion,Lista, Reproduccion
from django.contrib.auth import get_user_model

#artista
class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Artista
        fields=['id','nombre']

#album
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model=Album
        fields=['id','artista','nombre','anio']

#cancion
class CancionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cancion
        fields=['id','album','nombre','duracion','genero','colaboradores','url']

#lista
class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lista
        fields=['id','nombre',"canciones"]

#reproduccion
class ReproduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reproduccion
        fields=['id','cancion','fecha']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=['id','username','email']