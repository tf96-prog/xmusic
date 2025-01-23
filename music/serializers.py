from rest_framework import serializers
from music.models import Artista,Album

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