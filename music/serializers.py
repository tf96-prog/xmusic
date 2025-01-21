from rest_framework import serializers
from music.models import Artista

class ArtistaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombre=serializers.CharField(max_length=150)

    def create(self, validated_data):
        """
        Create and return a new `Cancion` instance, given the validated data.
        """
        return Artista.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Cancion` instance, given the validated data.
        """
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.save()
        return instance