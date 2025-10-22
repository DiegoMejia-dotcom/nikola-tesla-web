from django.db import models

# Create your models here.

class Cursos (models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    duracion = models.DateTimeField()
    nivel = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='cursos', null=True, blank=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'