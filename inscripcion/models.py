from django.db import models
from usuario.models import Usuarios
from curso.models import Cursos
# Create your models here.

class Inscripcion (models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    progreso = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return f'{self.usuario} - {self.curso} ({self.progreso}%)'
    
    class Meta:
        verbose_name = 'inscripcion'
        verbose_name_plural = 'inscripciones'