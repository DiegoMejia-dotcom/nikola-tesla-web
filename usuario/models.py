from django.db import models
from django.core.validators import RegexValidator

class Usuarios(models.Model):
    ROLES = [
        ("EST", "Estudiante"),
        ("ADM", "Administrador"),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9,unique=True,validators=[RegexValidator(regex=r'^\d{9}$',message='El número de teléfono debe tener exactamente 9 dígitos numéricos.')])
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=200)
    fecha_registro = models.DateField(auto_now_add=True)
    rol = models.CharField(max_length=3, choices=ROLES, default="EST")

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.get_rol_display()})"
    
    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
