from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from music.models import Artista
from music.serializers import ArtistaSerializer
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def artista_list(request):
    """
    List all code artistas, or create a new artista.
    """
    if request.method == 'GET':
        artistas = Artista.objects.all()
        serializer = ArtistaSerializer(artistas, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        print(request.data)

@csrf_exempt
@api_view()
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