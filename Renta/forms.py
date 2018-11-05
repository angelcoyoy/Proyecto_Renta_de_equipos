from django import forms
from .models import Cliente, Equipo

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('nombre', 'nit', 'telefono', 'direccion', 'correo', 'fecha_de_rentacion', 'equipos')

        def __init__ (self, *args, **kwargs):
            super(ClienteForm, self).__init__(*args, **kwargs)
            self.fields["equipos"].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields["equipos"].help_text = "Ingrese los Equipos a rentar"
            self.fields["equipos"].queryset = Equipo.objects.all()

class EquipoForm(forms.ModelForm):

    class Meta:
        model = Equipo
        fields = ('nombre', 'tipo', 'marca', 'precio', 'modelo')

        def __init__ (self, *args, **kwargs):
            super(EquipoForm, self).__init__(*args, **kwargs)
            self.fields["clientes"].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields["clientes"].help_text = "Ingrese los clientes de los equipos rentados"
            self.fields["clientes"].queryset = Cliente.objects.all()
