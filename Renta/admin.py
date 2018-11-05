from django.contrib import admin
from Renta.models import Equipo, EquipoAdmin, Cliente, ClienteAdmin

#Registramos nuestras clases principales.
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Cliente, ClienteAdmin)
