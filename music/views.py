from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from music.models import Artista
from music.serializers import ArtistaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


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
        
        