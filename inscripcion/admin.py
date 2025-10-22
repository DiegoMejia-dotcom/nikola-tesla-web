from django.contrib import admin
from .models import Inscripcion
# Register your models here.

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'curso', 'fecha_inscripcion', 'progreso')
    search_fields = ('usuario__nombre', 'curso__titulo')
    list_filter = ('fecha_inscripcion', 'curso')
    ordering = ('-fecha_inscripcion',)
