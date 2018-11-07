from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from Renta.models import Cliente, Equipo, Rentacion
from .forms import ClienteForm, EquipoForm
from django.shortcuts import redirect

def pagina_principal(request):
    return render(request, 'principal/pagina_principal.html')

def acerca_de_nosotros(request):
    return render(request, 'principal/acerca_de_nosotros.html')

def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipo/lista_equipos.html', {'equipos': equipos})

def detalle_equipo(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    return render(request, 'equipo/detalle_equipo.html', {'equipo': equipo})

def equipo_nuevo(request):
    if request.method == "POST":
        formulario = EquipoForm(request.POST)
        if formulario.is_valid():
            equipo = Equipo.objects.create(nombre=formulario.cleaned_data['nombre'], tipo = formulario.cleaned_data['tipo'], marca = formulario.cleaned_data['marca'], precio = formulario.cleaned_data['precio'], modelo = formulario.cleaned_data['modelo'])
            for cliente_id in request.POST.getlist('clientes'):
                rentacion = Rentacion(equipo_id=equipo_id, cliente_id = cliente.id)
                rentacion.save()
            messages.add_message(request, messages.SUCCESS, 'Equipo Guardado Exitosamente')
            return redirect('lista_equipos')
    else:
        formulario = EquipoForm()
    return render(request, 'equipo/editar_equipo.html', {'formulario': formulario})

def editar_equipo(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    if request.method == "POST":
        formulario = EquipoForm(request.POST, instance=equipo)
        if formulario.is_valid():
            equipo = formulario.save(commit=False)
            equipo.save()
            return redirect('detalle_equipo', pk=equipo.pk)
    else:
        formulario = EquipoForm(instance=equipo)
    return render(request, 'equipo/editar_equipo.html', {'formulario': formulario})

def eliminar_equipo(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    equipo.delete()
    return redirect('lista_equipos')

def lista_clientes(request):
    clientes = Cliente.objects.all()
    equipos = Equipo.objects.all()
    return render(request, 'cliente/lista_clientes.html', {'clientes': clientes, 'equipos': equipos})

def detalle_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    equipos = Equipo.objects.all()
    return render(request, 'cliente/detalle_cliente.html', {'cliente': cliente, 'equipos': equipos})

def cliente_nuevo(request):
    if request.method == "POST":
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            cliente = Cliente.objects.create(nombre=formulario.cleaned_data['nombre'], nit = formulario.cleaned_data['nit'], telefono = formulario.cleaned_data['telefono'], direccion = formulario.cleaned_data['direccion'], correo = formulario.cleaned_data['correo'], fecha_de_rentacion = formulario.cleaned_data['fecha_de_rentacion'])
            for equipo_id in request.POST.getlist('equipos'):
                rentacion = Rentacion(equipo_id=equipo_id, cliente_id = cliente.id)
                rentacion.save()
            messages.add_message(request, messages.SUCCESS, 'Cliente Guardado Exitosamente')
            return redirect('lista_clientes')
    else:
        formulario = ClienteForm()
    return render(request, 'cliente/editar_cliente.html', {'formulario': formulario})

def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        formulario = ClienteForm(request.POST, instance=cliente)
        if formulario.is_valid():
            cliente = formulario.save(commit=False)
            cliente.save()
            return redirect('detalle_cliente', pk=cliente.pk)
    else:
        formulario = ClienteForm(instance=cliente)
    return render(request, 'cliente/editar_cliente.html', {'formulario': formulario})

def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect('lista_clientes')
