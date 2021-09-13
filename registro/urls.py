from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiResumen, name='api-resumen'),
    path('clientes-lista',views.clientesLista, name='clientes-lista'),
    path('cliente-detalle/<str:pk>/',views.clienteDetalle, name='cliente-detalle'),
    path('cliente-crear',views.clienteCrear, name='cliente-crear'),
    path('cliente-actualizar/<str:pk>',views.clienteActualizar, name='cliente-actualizar'),
    path('cliente-borrar/<str:pk>',views.clienteBorrar, name='cliente-borrar'),
]