from django.contrib import admin
from .models import Alumno, Asistencia, Cursos, Periodos, Ingreso_notas

# Register your models here.
@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','status']

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Cursos)
class CursosAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status']


@admin.register(Periodos)
class PeriodosAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


#usuario: sergio123
#contraseña: idatsdeveloper1


@admin.register(Ingreso_notas)
class IngresonotasAdmin(admin.ModelAdmin):
    list_display = ['id', 'alumno', 'curso', 'nota', 'periodo']