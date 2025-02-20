from django.db import models
from django.contrib.auth import get_user_model

class Artista(models.Model):
    
    nombre=models.CharField(max_length=150)

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ['nombre']

class Album(models.Model):
    artista=models.ForeignKey(Artista, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=150)
    anio=models.IntegerField()

    def __str__(self):
        return self.artista.nombre + " - " + self.nombre
    
    class Meta:
        ordering = ['artista','nombre']

class Cancion(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    usuario=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    nombre=models.CharField(max_length=150)
    duracion=models.IntegerField()
    genero=models.CharField(max_length=150)
    colaboradores=models.ManyToManyField(Artista)
    url=models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ['album','nombre']

class Lista(models.Model):
    usuario=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    nombre=models.CharField(max_length=150)
    canciones=models.ManyToManyField(Cancion)

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ['nombre']


class Reproduccion(models.Model):
    cancion=models.ForeignKey(Cancion, on_delete=models.CASCADE)
    fecha=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cancion.nombre + " - " + self.fecha.strftime("%d/%m/%y, %H:%M:%S")
    
    class Meta:
        ordering = ['cancion']