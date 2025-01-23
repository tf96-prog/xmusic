from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from music.models import Artista, Album
from music.serializers import ArtistaSerializer, AlbumSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


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
        artista = self.get_object(pk)
        serial=ArtistaSerializer(artista,data=request.data)
        if serial.is_valid():
            serial.save()
            return JsonResponse(serial.data)
        return Response(serial.errors, status=400)
    def delete(self, request,pk):
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
        
        