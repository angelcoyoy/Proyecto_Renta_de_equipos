from django import forms
from .models import Cliente, Equipo

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = [
            'nombre',
            'nit',
            'telefono',
            'direccion',
            'correo',
            'fecha_de_rentacion',
            'equipos',
        ]
        labels = {
            'nombre': 'Nombre',
            'nit': 'NIT',
            'telefono': 'Telefono',
            'direccion': 'Direccion',
            'correo': 'Correo',
            'fecha_de_rentacion': 'Fecha de rentacion de equipos',
            'equipos': 'Equipos rentados',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'nit': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_de_rentacion': forms.TextInput(attrs={'class':'form-control'}),
            'equipos' : forms.CheckboxSelectMultiple(),
        }

class EquipoForm(forms.ModelForm):

    class Meta:
        model = Equipo
        fields = [
            'nombre',
            'tipo',
            'marca',
            'modelo',
            'precio',
        ]
        labels = {
            'nombre': 'Nombre del equipo',
            'tipo': 'Tipo de equipo',
            'marca': 'Marca del equipo',
            'modelo': 'Modelo del equipo',
            'precio': 'Precio de renta del equipo',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.TextInput(attrs={'class':'form-control'}),
            'marca': forms.TextInput(attrs={'class':'form-control'}),
            'modelo': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.TextInput(attrs={'class':'form-control'}),
        }
