from django.urls import path
from .views import CursosList

urlpatterns = [
    path('', CursosList.as_view(), name='cursos_list'),
]
