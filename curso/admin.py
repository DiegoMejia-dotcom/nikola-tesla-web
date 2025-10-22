from django.contrib import admin
from .models import Cursos
# Register your models here.

@admin.register(Cursos)

class CursosAdmin (admin.ModelAdmin):
    list_display = ('titulo', 'nivel', 'duracion', 'estado', 'fecha_creacion')
    search_fields = ('titulo', 'nivel')
    list_filter = ('estado', 'nivel')
    ordering =('-fecha_creacion',)