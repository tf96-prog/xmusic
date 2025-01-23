from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from music.models import Artista, Album, Cancion
from music.serializers import ArtistaSerializer, AlbumSerializer, CancionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate


#usuario

class UserLoginView(APIView):
    authentication_classes=[TokenAuthentication]

    def post(self, request):
        
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
        

#artista

class ArtistaListView(APIView):
    """
    List all code artistas, or create a new artista.
    """
    
    def get(self, request):

        artistas = Artista.objects.all()
        serializer = ArtistaSerializer(artistas, many=True)
        return JsonResponse(serializer.data, safe=False)
        
        
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
    Retrieve, update or delete a code artista.
    """

    def get_object(self, pk):
        try:
            return Artista.objects.get(pk=pk)
        except Artista.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request,pk):
        artista = self.get_object(pk)
        if artista is None:
            return Response(status=404)
        serializer = ArtistaSerializer(artista)
        return JsonResponse(serializer.data)
    def put(self, request,pk):

        if request.user.is_superuser:
            artista = self.get_object(pk)
            serial=ArtistaSerializer(artista,data=request.data)
            if serial.is_valid():
                serial.save()
                return JsonResponse(serial.data)
            return Response(serial.errors, status=400)
        return Response(serial.errors, status=401)
    def delete(self, request,pk):

        if request.user.is_superuser:
            artista = self.get_object(pk)
            serilier=ArtistaSerializer(data=request.data)
            if serilier.is_valid():
                if artista.pk==pk:
                    artista.delete()
                    return Response(serilier.data,status=204)
                else:
                    return JsonResponse({"error": "Los datos del objeto no coinciden con el ID solicitado"}, status=400)
            else:
                return JsonResponse(serilier.errors, status=400)
        return Response(serilier.errors, status=401)


#album

class AlbumListView(APIView):
    """
    List all code albums, or create a new album.
    """
    
    def get(self, request):

        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return JsonResponse(serializer.data, safe=False)
        
        
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
    Retrieve, update or delete a code album.
    """

    def get_object(self, pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request,pk):
        album = self.get_object(pk)
        if album is None:
            return Response(status=404)
        serializer = AlbumSerializer(album)
        return JsonResponse(serializer.data)
    def put(self, request,pk):
        album = self.get_object(pk)
        serial=AlbumSerializer(album,data=request.data)
        if serial.is_valid():
            serial.save()
            return JsonResponse(serial.data)
        return Response(serial.errors, status=400)
    def delete(self, request,pk):
        album = self.get_object(pk)
        serilier=AlbumSerializer(data=request.data)
        if serilier.is_valid():
            if album.pk==pk:
                album.delete()
                return Response(serilier.data,status=204)
            else:
                return JsonResponse({"error": "Los datos del objeto no coinciden con el ID solicitado"}, status=400)
        else:
            return JsonResponse(serilier.errors, status=400)
        
#cancion
class CancionListView(APIView):
    """
    List all code canciones, or create a new cancion.
    """
    
    def get(self, request):

        canciones = Cancion.objects.all()
        serializer = CancionSerializer(canciones, many=True)
        return JsonResponse(serializer.data, safe=False)
        
        
    def post(self, request):
        
        if request.user.is_superuser or request.user.is_authenticated:
            cancion=Cancion()
            if request.user==cancion.usuario and cancion.colaboradores.exists:
                serial=CancionSerializer(data=request.data)
                if serial.is_valid():
                    serial.save()
                    return JsonResponse(serial.data, safe=False,status=201)
            return Response(serial.errors, safe=False,status=401)
        else:
            return Response({"mensaje":"Acceso a creacion de canciones solo a administradores"}, status=403)
        
class CancionDetailView(APIView):
    """
    Retrieve, update or delete a code album.
    """

    def get_object(self, pk):
        try:
            return Cancion.objects.get(pk=pk)
        except Cancion.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request,pk):
        cancion = self.get_object(pk)
        if cancion is None:
            return Response(status=404)
        serializer = CancionSerializer(cancion)
        return JsonResponse(serializer.data)
    def put(self, request,pk):

        if request.user.is_superuser:
            cancion = self.get_object(pk)
            if request.user==cancion.usuario:
                serial=CancionSerializer(cancion,data=request.data)
                if serial.is_valid():
                    serial.save()
                    return JsonResponse(serial.data)
                return Response(serial.errors, status=400)
            return Response(serial.errors, status=400)
        return Response(serial.errors, status=401)
    def delete(self, request,pk):

        if request.user.is_superuser:
            cancion = self.get_object(pk)
            if request.user==cancion.usuario:
                serilier=CancionSerializer(cancion=request.data)
                if serilier.is_valid():
                    if cancion.pk==pk:
                        cancion.delete()
                        return Response(serilier.data,status=204)
                    else:
                        return JsonResponse({"error": "Los datos del objeto no coinciden con el ID solicitado"}, status=400)
                else:
                    return JsonResponse(serilier.errors, status=400)
            return JsonResponse(serilier.errors, status=400)
        return JsonResponse(serilier.errors, status=401)
