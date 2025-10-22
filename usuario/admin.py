from django.contrib import admin
from .models import Usuarios
# Register your models here.

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telefono', 'email', 'fecha_registro')
    search_fields = ('nombre', 'apellido', 'email')
    list_filter = ('fecha_registro',)
    ordering = ('-fecha_registro',)
