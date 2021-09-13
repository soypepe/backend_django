from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cliente
from .serializador import ClienteSerializador

@api_view(['GET'])
def apiResumen(request):
  api_urls={
    'Lista':'/clientes-lista',
    'Vista de detalles':'/cliente-detalle/<str:pk>',
    'Crear':'/cliente-crear',
    'Actualizar':'/cliente-actualizar/<str:pk>',
    'Borrar':'/cliente-borrar/<str:pk>',
  }
  return Response(api_urls)

@api_view(['get'])
def clientesLista(request):
  clientes=Cliente.objects.all()
  serializador = ClienteSerializador(clientes, many=True)
  return Response(serializador.data)

@api_view(['get'])
def clienteDetalle(request,pk):
  clientes=Cliente.objects.get(id=pk)
  serializador = ClienteSerializador(clientes, many=False)
  return Response(serializador.data)

@api_view(['post'])
def clienteCrear(request):
  serializador = ClienteSerializador(data=request.data)
  if serializador.is_valid():
    serializador.save()
  return Response(serializador.data)

@api_view(['put'])
def clienteActualizar(request,pk):
  cliente=Cliente.objects.get(id=pk)
  serializador = ClienteSerializador(instance=cliente, data=request.data)
  if serializador.is_valid():
    serializador.save()
  return Response(serializador.data)

@api_view(['delete'])
def clienteBorrar(request,pk):
  cliente=Cliente.objects.get(id=pk)
  cliente.delete()
  return Response('Borrado correctamente')