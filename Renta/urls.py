from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    path('', views.pagina_principal, name='pagina_principal'),
    url(r'^principal/acerca/$', views.acerca_de_nosotros, name='acerca_de_nosotros'),
    url(r'^equipo/lista/$', views.lista_equipos, name='lista_equipos'),
    path('equipo/<int:pk>/', views.detalle_equipo, name='detalle_equipo'),
    url(r'^equipo/nuevo/$', views.equipo_nuevo, name='equipo_nuevo'),
    path('equipo/<int:pk>/edit/', views.editar_equipo, name='editar_equipo'),
    url(r'^equipo/(?P<pk>\d+)/eliminar/$', views.eliminar_equipo, name='eliminar_equipo'),
    url(r'^cliente/lista/$', views.lista_clientes, name='lista_clientes'),
    path('cliente/<int:pk>/', views.detalle_cliente, name='detalle_cliente'),
    url(r'^cliente/nuevo/$', views.cliente_nuevo, name='cliente_nuevo'),
    path('cliente/<int:pk>/edit/', views.editar_cliente, name='editar_cliente'),
    url(r'^cliente/(?P<pk>\d+)/eliminar/$', views.eliminar_cliente, name='eliminar_cliente'),
    ]
