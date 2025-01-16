from django.db import models

class Usuario(models.Model):
    id=models.IntegerField(primary_key=True)
    email=models.CharField(max_length=150)
    contrasenia=models.CharField(max_length=150)

class Lista(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=150)
    n_canciones=models.IntegerField()

class Cancion(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=150)
    duracion=models.IntegerField()
    genero=models.CharField(max_length=150)

class Artista(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=150)

class Album(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=150)
    anio=models.IntegerField()

class Reproduccion(models.Model):
    id_cancion=models.IntegerField()
    fecha=models.DateTimeField()
