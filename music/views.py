from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from music.models import Artista
from music.serializers import ArtistaSerializer
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

@api_view(['GET','POST'])
def artista_list(request):
    """
    List all code artistas, or create a new artista.
    """
    print(request.user)
    if request.method == 'GET':

        

            artistas = Artista.objects.all()
            serializer = ArtistaSerializer(artistas, many=True)
            return JsonResponse(serializer.data, safe=False)
        
        
    if request.method == 'POST':
        
        if request.user.is_superuser:

            serial=ArtistaSerializer(data=request.data)
            if serial.is_valid():
                serial.save()
                return JsonResponse(serial.data, safe=False,status=201)
            
        else:
            return Response({"mensaje":"Acceso a creacion de artistas solo a administradores"}, status=403)
        
        
        return JsonResponse(serial.errors, safe=False,status=400)

        

@api_view(['GET','PUT'])
def artista_detail(request, pk):
    """
    Retrieve, update or delete a code artista.
    """
    try:
        artista = Artista.objects.get(pk=pk)
    except Artista.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArtistaSerializer(artista)
        return JsonResponse(serializer.data)
    if request.method == 'PUT':
        serial=ArtistaSerializer(artista,data=request.data)
        if serial.is_valid():
            serial.save()
            return JsonResponse(serial.data)
        return Response(serial.errors, status=400)
        
        