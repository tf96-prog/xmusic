from django.shortcuts import render
from django.http import JsonResponse
from music.models import Artista, Album, Cancion, Lista
from music.serializers import ArtistaSerializer, AlbumSerializer, CancionSerializer, ListaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate


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
        

#artista

class ArtistaListView(APIView):
    """
    Muestra la lista de artistas, y/o crea artistas
    """
    
    #mostar lista de artistas
    def get(self, request):

        artistas = Artista.objects.all()
        serializer = ArtistaSerializer(artistas, many=True)
        return JsonResponse(serializer.data, safe=False)
        
    #añade artista
    def post(self, request):
        
        if request.user.is_superuser:

            serial=ArtistaSerializer(data=request.data)
            if serial.is_valid():
                serial.save()
                return JsonResponse(serial.data, safe=False,status=201)
            
        else:
            return Response({"mensaje":"Acceso a creacion de artistas solo a administradores"}, status=403)
        
        
        return JsonResponse(serial.errors, safe=False,status=400)

        


class ArtistaDetailView(APIView):
    """
    Obtiene artista mediante id , actualiza y/o elimina artistas
    """

    #obtiene artista mediante id o None si no existe
    def get_object(self, pk):

        
        try:
            return Artista.objects.get(pk=pk)
        except Artista.DoesNotExist:            
            return None


    #valida si el artista es nulo
    def get(self, request,pk):
        artista = self.get_object(pk)
        if artista is None:
            return Response(status=404)
        serializer = ArtistaSerializer(artista)
        return JsonResponse(serializer.data)
    
    #actualiza artista
    def put(self, request,pk):

        if request.user.is_superuser:
            artista = self.get_object(pk)
            if artista is None:
                return Response(status=404)
            serial=ArtistaSerializer(artista, data=request.data)
            if serial.is_valid():
                serial.save()
                return JsonResponse(serial.data)
            return JsonResponse(serial.errors, status=400)
        else:
            return JsonResponse({"mensaje":"Acceso no autorizado"}, status=401)
    

    #elimina artista
    def delete(self, request,pk):
        if request.user.is_superuser:
            artista = self.get_object(pk)
            if artista is not None:
                artista.delete()
                return JsonResponse({"mensaje":"Artista eliminado"}, status=200)
            else:
                return JsonResponse({"mensaje":"El artista es nulo"},status=404)
        else:
            return JsonResponse({"mensaje":"Acceso no autorizado"}, status=401)


#album

class AlbumListView(APIView):
    """
    Muestra la lista de Album, y/o crea Albumes
    """
    
    #mostrar la lista de albumes
    def get(self, request):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return JsonResponse(serializer.data, safe=False)
        
        
    #añade album
    def post(self, request):
        
        if request.user.is_superuser:

            serial=AlbumSerializer(data=request.data)
            if serial.is_valid():
                serial.save()
                return JsonResponse(serial.data, safe=False,status=201)
            
        else:
            return Response({"mensaje":"Acceso a creacion de albumes solo a administradores"}, status=403)
        
        
        return JsonResponse(serial.errors, safe=False,status=400)

        


class AlbumDetailView(APIView):
    """
    Obtiene album mediante id , actualiza y/o elimina albumes
    """
    #obtiene album mediante id o None si no existe
    def get_object(self, pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            return None

    #valida si el album es nulo
    def get(self, request,pk):
        album = self.get_object(pk)
        if album is None:
            return Response(status=404)
        serializer = AlbumSerializer(album)
        return JsonResponse(serializer.data)

    #actualiza album
    def put(self, request,pk):
        album = self.get_object(pk)
        if request.user.is_superuser:
            if album is None:
                return Response(status=404)
            serial=AlbumSerializer(album,data=request.data)
            if serial.is_valid():
                serial.save()
                return JsonResponse(serial.data)
            return Response(serial.errors, status=400)
        return JsonResponse({"mensaje":"Acceso no autorizado"},status=401)
    
    #elimina album
    def delete(self, request,pk):
        album = self.get_object(pk)
        if request.user.is_superuser:
            if album is None:
               return JsonResponse({"mensaje":"El album es nulo"}, status=404)
            album.delete()
            return JsonResponse({"mensaje":"Album eliminado"}, status=200)
        return JsonResponse({"mensaje":"Acceso no autorizado"},status=401)

        
#cancion

class CancionListView(APIView):
    """
    Muestra la lista de canciones, y/o crea canciones
    """
    
    #mostrar la lista de canciones
    def get(self, request):

        canciones = Cancion.objects.all()
        serializer = CancionSerializer(canciones, many=True)
        return JsonResponse(serializer.data, safe=False)
        
    #añade cancion
    def post(self, request):
        
        if request.user.is_authenticated:
            
            serial=CancionSerializer(data=request.data)
            if serial.is_valid():
                cancion=serial.save(usuario=request.user)
                return Response(CancionSerializer(cancion).data,status=201)
            return JsonResponse({"mensaje":"Cancion no valida"}, status=400)
            
        else:
            return Response({"mensaje":"Acceso a creacion de canciones solo a administradores"}, status=403)
        
class CancionDetailView(APIView):
    """
    Obtiene cancion mediante id , actualiza y/o elimina canciones
    """

    #obtiene cancion mediante id o None si no existe
    def get_object(self, pk):
        try:
            return Cancion.objects.get(pk=pk)
        except Cancion.DoesNotExist:
            return None

    #validar si la cancion es nula
    def get(self, request,pk):
        cancion = self.get_object(pk)
        if cancion is None:
            return Response(status=404)
        serializer = CancionSerializer(cancion)
        return JsonResponse(serializer.data)

    #actualiza cancion
    def put(self, request,pk):
        if request.user.is_authenticated:
            cancion = self.get_object(pk)
            if cancion is None:
                return Response({"mensaje": "Canción no encontrada"}, status=404)
            if request.user != cancion.usuario and not request.user.is_superuser:
                return Response({"mensaje": "No tienes permisos para actualizar esta canción"}, status=403)
            serial=CancionSerializer(cancion,data=request.data)
            if serial.is_valid():
                cancion_actualizada = serial.save(usuario=cancion.usuario)
                return Response(CancionSerializer(cancion_actualizada).data, status=200)
            return Response(serial.errors, status=400)
        return Response(serial.errors, status=401)

    #elimina cancion
    def delete(self, request,pk):
        if request.user.is_authenticated:
            cancion = self.get_object(pk)
            if cancion is None:
                return JsonResponse({"mensaje":"La cancion no existe"}, status=404)
            if request.user != cancion.usuario and not request.user.is_superuser:
                return Response({"mensaje": "No tienes permisos para eliminar esta canción"}, status=403)
            cancion.delete()
            return JsonResponse({"mensaje":"Cancion eliminada"}, status=200)
        return JsonResponse({"mensaje": "Acceso no autorizado"}, status=401)


#lista de reproduccion
class ListaListView(APIView):
    """
    Muestra la lista de listas_r, y/o crea listas_r
    """
    
    #mostrar la lista de listas_r
    def get(self, request):
        
        if request.user.is_anonymous:
            return JsonResponse({"mensaje":"Las listas solo pueden ser vistas por usuarios autenticados"},status=400)
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
    def post(self, request):
        
        if request.user.is_authenticated:
            
            serial=ListaSerializer(data=request.data)
            if serial.is_valid():
                lista=serial.save(usuario=request.user)
                return Response(ListaSerializer(lista).data,status=201)
            return JsonResponse({"mensaje":"Lista no valida"}, status=400)
            
        else:
            return Response({"mensaje":"Acceso a creacion de listas solo a usuarios autenticados"}, status=403)


class ListaDetailView(APIView):
    """
    Obtiene lista_r mediante id , actualiza y/o elimina lista_r
    """

    #obtiene lista_r mediante id o None si no existe
    def get_object(self, pk):
        try:
            return Lista.objects.get(pk=pk)
        except Lista.DoesNotExist:
            return None

    #validar si la lista_r es nula
    def get(self, request,pk):
        lista = self.get_object(pk)
        if lista is None:
            return Response(status=404)
        serializer = ListaSerializer(lista)
        return JsonResponse(serializer.data)

    #actualiza lista_r
    def put(self, request,pk):
        if request.user.is_authenticated:
            lista = self.get_object(pk)
            if lista is None:
                return Response({"mensaje": "Lista no encontrada"}, status=404)
            if request.user != lista.usuario and not request.user.is_superuser:
                return Response({"mensaje": "No tienes permisos para actualizar esta Lista"}, status=403)
            serial=ListaSerializer(lista,data=request.data)
            if serial.is_valid():
                lista_actualizada = serial.save(usuario=lista.usuario)
                return Response(ListaSerializer(lista_actualizada).data, status=200)
            return Response(serial.errors, status=400)
        return Response({"mensaje":"Acceso no autorizado"}, status=403)

    #elimina lista_r
    def delete(self, request,pk):
        if request.user.is_authenticated:
            lista = self.get_object(pk)
            if lista is None:
                return JsonResponse({"mensaje":"La lista no existe"}, status=404)
            if request.user != lista.usuario and not request.user.is_superuser:
                return Response({"mensaje": "No tienes permisos para eliminar esta lista"}, status=403)
            lista.delete()
            return JsonResponse({"mensaje":"Lista eliminada"}, status=200)
        return JsonResponse({"mensaje": "Acceso no autorizado"}, status=401)