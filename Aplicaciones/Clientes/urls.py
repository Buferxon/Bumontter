from django.urls import path

from Aplicaciones.Clientes.views import ClientesListView, eliminar_cliente, registrar_cliente, edicion_cliente, editar_cliente, permission_required



urlpatterns = [
    path('', ClientesListView.as_view(), name='gestion_clientes'),
    path('registrarCliente/', registrar_cliente),
    path('eliminacionClientes/<int:id>', eliminar_cliente),
    path('edicionClientes/<int:id>', edicion_cliente),
    path('edicionClientes/editarCliente/', editar_cliente)
]
