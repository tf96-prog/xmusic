from rest_framework import serializers
from music.models import Artista,Album,Cancion,Lista

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
        fields=['id','album','nombre','duracion','genero','colaboradores']

#lista
class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lista
        fields=['id','nombre',"canciones"]
