from django.shortcuts import render
from django.http import JsonResponse
from music.models import Artista, Album, Cancion, Lista,Reproduccion
from music.serializers import ArtistaSerializer, AlbumSerializer, CancionSerializer, ListaSerializer, ReproduccionSerializer,UsuarioSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from django.contrib.auth import get_user_model


#usuario

class UserLoginView(APIView):
    authentication_classes=[TokenAuthentication]
    
    #autenticacion de usuario mediante creacion de token

    def post(self, request):
        
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Credenciales invalidas'}, status=401) 


class UsuarioView(APIView):
    
    def get(self,request):
        usuario=request.user
        serializer=UsuarioSerializer(usuario)
        return Response(serializer.data)


#artista

class ArtistaViewSet(viewsets.ViewSet):
    """
    Muestra la lista de artistas, y/o crea artistas, actualiza y elimina
    """
    
    #mostar lista de artistas
    def list(self, request):

        artistas = Artista.objects.all()
        serializer = ArtistaSerializer(artistas, many=True)
        return Response(serializer.data)
        
    #añade artista
    def create(self, request):
        
        if request.user.is_superuser:

            serial=ArtistaSerializer(data=request.data)
            if serial.is_valid():
                serial.save()
                return JsonResponse(serial.data, safe=False,status=201)
            
        else:
            return Response({"mensaje":"Acceso a creacion de artistas solo a administradores"}, status=403)
        
        
        return JsonResponse(serial.errors, safe=False,status=400)


    #obtiene artista mediante id
    def retrieve(self, request,pk):

        artistas = Artista.objects.all()
        artista=get_object_or_404(artistas,pk=pk)
        serializer=ArtistaSerializer(artista)
        return Response(serializer.data)
    
    #actualiza artista
    def update(self, request,pk):

        if request.user.is_superuser:
            artista = Artista.objects.get(pk=pk)
            serial=ArtistaSerializer(artista, data=request.data)
            if serial.is_valid():
                serial.save()
                return JsonResponse(serial.data)
            return JsonResponse(serial.errors, status=400)
        else:
            return JsonResponse({"mensaje":"Acceso no autorizado"}, status=401)
    

    #elimina artista
    def destroy(self, request,pk):
        if request.user.is_superuser:
            artista = Artista.objects.get(pk=pk)
            if artista is not None:
                artista.delete()
                return JsonResponse({"mensaje":"Artista eliminado"}, status=200)
            else:
                return JsonResponse({"mensaje":"El artista es nulo"},status=404)
        else:
            return JsonResponse({"mensaje":"Acceso no autorizado"}, status=401)


#album

class AlbumViewSet(viewsets.ViewSet):
    """
    Muestra la lista de Album, y/o crea Albumes, actualiza y elimina
    """
    
    #mostrar la lista de albumes
    def list(self, request):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)
        
        
    #añade album
    def create(self, request):
        
        if request.user.is_superuser:

            serial=AlbumSerializer(data=request.data)
            if serial.is_valid():
                serial.save()
                return JsonResponse(serial.data, safe=False,status=201)
            
        else:
            return Response({"mensaje":"Acceso a creacion de albumes solo a administradores"}, status=403)
        
        
        return JsonResponse(serial.errors, safe=False,status=400)
    
    #obtiene album mediante id
    def retrieve(self,request, pk):
        albumes = Album.objects.all()
        album=get_object_or_404(albumes,pk=pk)
        serializer=AlbumSerializer(album)
        return Response(serializer.data)


    #actualiza album
    def update(self, request,pk):
        
        if request.user.is_superuser:
            album = Album.objects.get(pk=pk)
            serial=AlbumSerializer(album,data=request.data)
            if serial.is_valid():
                serial.save()
                return JsonResponse(serial.data)
            return Response(serial.errors, status=400)
        else:
            return JsonResponse({"mensaje":"Acceso no autorizado"},status=401)
    
    #elimina album
    def destroy(self, request,pk):
        
        if request.user.is_superuser:
            album = Album.objects.get(pk=pk)
            album.delete()
            return JsonResponse({"mensaje":"Album eliminado"}, status=200)
        return JsonResponse({"mensaje":"Acceso no autorizado"},status=401)

        
#cancion

class CancionViewSet(viewsets.ViewSet):
    """
    Muestra la lista de canciones, y/o crea canciones, actualiza y/o elimina
    """
    
    #mostrar la lista de canciones
    def list(self, request):

        canciones = Cancion.objects.all()
        serializer = CancionSerializer(canciones, many=True)
        return Response(serializer.data)
        
    #añade cancion
    def create(self, request):
        
        if request.user.is_authenticated:
            
            serial=CancionSerializer(data=request.data)
            if serial.is_valid():
                cancion=serial.save(usuario=request.user)
                return Response(CancionSerializer(cancion).data,status=201)
            return JsonResponse({"mensaje":"Cancion no valida"}, status=400)
        return Response({"mensaje":"Acceso a creacion de canciones solo a autenticados"}, status=403)
    
    #obtiene cancion mediante id
    def retrieve(self, request,pk):
        canciones = Cancion.objects.all()
        cancion=get_object_or_404(canciones,pk=pk)
        serializer=CancionSerializer(cancion)
        return Response(serializer.data)


    #actualiza cancion
    def update(self, request,pk):
        if request.user.is_authenticated:
            cancion = Cancion.objects.get(pk=pk)
            serial=CancionSerializer(cancion,data=request.data)
            if request.user != cancion.usuario and not request.user.is_superuser:
                return Response({"mensaje": "No tienes permisos para actualizar esta canción"}, status=403)
            
            if serial.is_valid():
                cancion_actualizada = serial.save(usuario=cancion.usuario)
                return Response(CancionSerializer(cancion_actualizada).data, status=200)
            return Response(serial.errors, status=400)
        return Response({"mensaje":"Acceso no autorizado"}, status=401)

    #elimina cancion
    def destroy(self, request,pk):
        if request.user.is_authenticated:
            cancion = Cancion.objects.get(pk=pk)
            if request.user != cancion.usuario and not request.user.is_superuser:
                return Response({"mensaje": "No tienes permisos para eliminar esta canción"}, status=403)
            cancion.delete()
            return JsonResponse({"mensaje":"Cancion eliminada"}, status=200)
        return JsonResponse({"mensaje": "Acceso no autorizado"}, status=401)
    
    #añade reproduccion
    @action(detail=True, methods=['post'])
    def add_reproduccion(self, request,pk):
        try:
            cancion=Cancion.objects.get(pk=pk)
        except Cancion.DoesNotExist:
            return Response({"mensaje": "La canción no existe."}, status=404)
        reproduccion = Reproduccion.objects.create(cancion=cancion)
        serializer=ReproduccionSerializer(reproduccion)
        return Response(serializer.data,status=201)


#lista de reproduccion
class ListaViewSet(viewsets.ViewSet):
    """
    Muestra la lista de listas_r, y/o crea listas_r, actualiza y elimina
    """
    
    #mostrar la lista de listas_r
    def list(self, request):
        
        if request.user.is_anonymous:
            return JsonResponse({"mensaje":"Las listas solo pueden ser vistas por usuarios autenticados"},status=403)
        if request.user.is_authenticated:
            listas=Lista.objects.filter(usuario=request.user.id)
            serializer = ListaSerializer(listas, many=True)
            return JsonResponse(serializer.data, safe=False, status=200)
        if request.user.is_superuser:
            listas = Lista.objects.all()
            serializer = ListaSerializer(listas, many=True)
            return JsonResponse(serializer.data,status=200)
        return Response(status=400)
        
        
        
    #añade lista_r
    def create(self, request):
        
        if request.user.is_authenticated:
            
            serial=ListaSerializer(data=request.data)
            if serial.is_valid():
                lista=serial.save(usuario=request.user)
                return Response(ListaSerializer(lista).data,status=201)
            return JsonResponse({"mensaje":"Lista no valida"}, status=400)
            
        else:
            return Response({"mensaje":"Acceso a creacion de listas solo a usuarios autenticados"}, status=403)

    #obtiene lista_r mediante id
    def retrieve(self, request,pk):
        listas = Lista.objects.all()
        lista=get_object_or_404(listas,pk=pk)
        serializer=ListaSerializer(lista)
        return Response(serializer.data)


    #actualiza lista_r
    def update(self, request,pk):
        if request.user.is_authenticated:
            lista = Lista.objects.get(pk=pk)
            if request.user != lista.usuario and not request.user.is_superuser:
                return Response({"mensaje": "No tienes permisos para actualizar esta Lista"}, status=403)
            serial=ListaSerializer(lista,data=request.data)
            if serial.is_valid():
                lista_actualizada = serial.save(usuario=lista.usuario)
                return Response(ListaSerializer(lista_actualizada).data, status=200)
            return Response(serial.errors, status=400)
        return Response({"mensaje":"Acceso no autorizado"}, status=403)

    #elimina lista_r
    def destroy(self, request,pk):
        if request.user.is_authenticated:
            lista = Lista.objects.get(pk=pk)
            if request.user != lista.usuario and not request.user.is_superuser:
                return Response({"mensaje": "No tienes permisos para eliminar esta lista"}, status=403)
            lista.delete()
            return JsonResponse({"mensaje":"Lista eliminada"}, status=200)
        return JsonResponse({"mensaje": "Acceso no autorizado"}, status=403)