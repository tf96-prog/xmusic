from django.contrib import admin
from .models import Artista,Album,Cancion,Lista,Reproduccion

admin.site.register(Artista)
admin.site.register(Album)
admin.site.register(Cancion)
admin.site.register(Lista)
admin.site.register(Reproduccion)

