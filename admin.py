from django.contrib import admin
from academia.models import Curso, Nuevoalumno, Catedratico
# Register your models here.

class NuevoalumnoAdmin(admin.ModelAdmin):
    list_display=("nombre", "apellido", "DPI", "nombreusuario", "email")
    search_fields = ("nombre", "DPI", "nombreusuario")

class CatedraticoAdmin(admin.ModelAdmin):
    list_display=("nombre", "apellido")
    search_fields = ("nombre", "apellido")

class CursoAdmin(admin.ModelAdmin):
    list_display=("nombrecurso", "codigo", "costo", "horario", "cupo", "catedratico")
    search_fields = ("nombrecurso", "codigo")

admin.site.register(Nuevoalumno, NuevoalumnoAdmin)
admin.site.register(Catedratico, CatedraticoAdmin)
admin.site.register(Curso, CursoAdmin)
