from django.db import models
from django.db.models.fields.files import ImageField
from django.db.models.query import FlatValuesListIterable
from django.contrib.auth.models import User

# Create your models here.

class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    status = models.IntegerField(default=1) 
    
    class Meta:
        db_table = 'alumnos'
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        ordering = ['id']

    def __str__(self):
        return self.name

class Asistencia(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    
    class Meta:
        db_table = 'asistencia'
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'
        ordering = ['id']

    def __str__(self):
        return self.name

class Cursos(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    status = models.IntegerField(default=1)

    class Meta:
        db_table = 'cursos'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['id']

    def __str__(self):
        return self.name

# class Notas(models.Model):
#     id = models.AutoField(primary_key=True)
#     nota_curso = models.IntegerField()

#     class Meta:
#         db_table = 'notas'
#         verbose_name = 'Nota'
#         verbose_name_plural = 'Notas'
#         ordering = ['id']

#     def __str__(self):
#         return self.nota_curso

class Periodos(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)

    
    class Meta:
        db_table = 'periodo'
        verbose_name = 'Periodo'
        verbose_name_plural = 'Periodos'
        ordering = ['id']

    def __str__(self):
        return self.name

class Ingreso_notas(models.Model):
    id = models.AutoField(primary_key=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    nota = models.CharField(max_length=2, blank=False, null=False)
    periodo = models.ForeignKey(Periodos, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ingresonotas'
        verbose_name = 'Ingreso Nota'
        verbose_name_plural = 'Ingreso Notas'
        ordering = ['id']

    def __str__(self):
        return self.nota
  
class Ingreso_asistencia(models.Model):
    id = models.AutoField(primary_key=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    asistencia = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    class_date = models.DateField()
    periodo = models.ForeignKey(Periodos, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ingresoasistencia'
        verbose_name = 'Ingreso Asistencia'
        verbose_name_plural = 'Ingreso Asistencias'
        ordering = ['id']

    
    
    
