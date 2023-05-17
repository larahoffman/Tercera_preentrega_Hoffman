from django.urls import path
from AppFinal import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('leerProductos', views.leer_productos, name="LeerProductos")
    # path('usuarios', views.usuarios, name="Usuarios"),
    # path('productos', views.productos, name="Productos"),
    # path('pedidos', views.pedidos, name="Pedidos"),
    # path('buscar', views.buscar, name="Buscar")
]