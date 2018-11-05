from django.db import models
from django.contrib import admin

# Create your models here.
class Equipo(models.Model):

    nombre  =   models.CharField(max_length=30)

    tipo    =   models.CharField(max_length=30)

    marca   =   models.CharField(max_length=30)

    precio  =   models.CharField(max_length=30)

    modelo  =   models.CharField(max_length=30)


    def __str__(self):

        return self.nombre

class Cliente(models.Model):

    nombre    =   models.CharField(max_length=60)

    nit       =   models.CharField(max_length=60)

    telefono  =   models.CharField(max_length=60)

    direccion =   models.CharField(max_length=60)

    correo    =   models.CharField(max_length=60)

    fecha_de_rentacion = models.DateField()

    equipos  =   models.ManyToManyField(Equipo, through='Rentacion')


    def __str__(self):

        return self.nombre

class Rentacion (models.Model):

    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class RentacionInLine(admin.TabularInline):

    model = Rentacion
    extra = 1

class EquipoAdmin(admin.ModelAdmin):

    inlines = (RentacionInLine,)


class ClienteAdmin (admin.ModelAdmin):

    inlines = (RentacionInLine,)
