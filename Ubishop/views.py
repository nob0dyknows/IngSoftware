# Ubishop/views.py

from django.http import JsonResponse
from .models import Ubicacion, Productos, Tienda

def ubicaciones(request):
    ubicaciones = Ubicacion.objects.all()
    data = [
        {
            'tienda': ubicacion.tienda.nombre,
            'descripcion': ubicacion.tienda.descripcion,
            'latitud': float(ubicacion.latitud),
            'longitud': float(ubicacion.longitud),
            'direccion': ubicacion.direccion,
            'tienda_id': ubicacion.tienda.id
        }
        for ubicacion in ubicaciones
    ]
    return JsonResponse(data, safe=False)

def productos_por_tienda(request, tienda_id):
    productos = Productos.objects.filter(tienda_id=tienda_id)
    data = [
        {
            'nombre_producto': producto.nombre_producto,
            'descripcion': producto.descripcion,
            'precio': float(producto.precio),
            'stock': producto.stock
        }
        for producto in productos
    ]
    return JsonResponse(data, safe=False)


def productos(request):
    productos_all = Productos.objects.all()
    data = [
        {
            'nombre_producto': producto.nombre_producto,
            'descripcion': producto.descripcion,
            'precio': float(producto.precio),
            'stock': producto.stock
        }
        for producto in productos_all
    ]
    return JsonResponse(data, safe=False)





def tiendas(request):
    tiendas = Tienda.objects.all()
    data = [
        {
            'nombre': tienda.nombre,
            'descripcion': tienda.descripcion,
            'propietario': tienda.propietario.nombre_usuario,
            'propietario_id': tienda.propietario.id
        }
        for tienda in tiendas
    ]
    return JsonResponse(data, safe=False)