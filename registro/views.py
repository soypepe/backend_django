from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
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
  try:
    clientes=Cliente.objects.all()
    serializador = ClienteSerializador(clientes, many=True)
    return Response({'datos':serializador.data, 'estado':200},status=status.HTTP_200_OK)
  except:
    return Response({'mensaje':'No se puede mostrar los clientes', 'estado':404}, status=status.HTTP_404_NOT_FOUND)

@api_view(['get'])
def clienteDetalle(request,pk):
  try:
    cliente=Cliente.objects.get(id=pk)
    serializador = ClienteSerializador(cliente, many=False)
    return Response({"datos":serializador.data, "estado":200}, status=status.HTTP_200_OK)
  except:
    return Response({"mensaje":'Cliente no encontrado', "estado":404}, status=status.HTTP_404_NOT_FOUND)

@api_view(['post'])
def clienteCrear(request):
  serializador = ClienteSerializador(data=request.data)
  if serializador.is_valid():
    serializador.save()
    return Response({"datos":serializador.data, "estado":200}, status=status.HTTP_201_CREATED)
  else:
    return Response({'datos':'hubo un error','estado':404}, status=status.HTTP_404_NOT_FOUND)

@api_view(['put'])
def clienteActualizar(request,pk):
  try:
    cliente=Cliente.objects.get(id=pk)
    serializador = ClienteSerializador(instance=cliente, data=request.data)
    if serializador.is_valid():
      serializador.save()
      return Response({'datos':serializador.data,'estado':200}, status=status.HTTP_200_OK)
  except:
    return Response({'mensaje':'Cliente no encontrado', 'estado':404}, status=status.HTTP_404_NOT_FOUND)

@api_view(['delete'])
def clienteBorrar(request,pk):
  try:
    cliente=Cliente.objects.get(id=pk)
    cliente.delete()
    return Response({'mensaje':'Borrado correctamente', 'estado':200}, status=status.HTTP_200_OK)
  except:
    return Response({'mensaje':'Cliente no encontrado', 'estado':404}, status=status.HTTP_404_NOT_FOUND)