from django.contrib import admin

from .models import Publicacion
from .models import Usuario
from .models import Hastag




class PublicacionAdmin(admin.ModelAdmin):
	fields = ['pub_date','publi']

class UsuarioAdmin(admin.ModelAdmin):
	fields = ['question','nombre','edad']

class HastagAdmin(admin.ModelAdmin):
	fields = ['publicaciones','hastag']



admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Hastag, HastagAdmin)