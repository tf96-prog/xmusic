from rest_framework import serializers
from music.models import Artista,Album,Cancion

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
        fields=['id','album','usuario','nombre','duracion','genero','colaboradores']