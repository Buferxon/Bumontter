from django.shortcuts import render, redirect
from .models import Cliente
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages


# def home(request):
#     clientes=Cliente.objects.all()
#     data = {
#         'titulo':'Gestion Clientes',
#         'clientes':clientes
#     }
#     # return render(request,"gestionClientes.html",{"clientes":clientes})
#     return render(request,"gestionClientes.html",data)

@method_decorator(login_required, name='dispatch')
@method_decorator(permission_required('clientes.view_cliente', login_url='/'), name='dispatch')
class ClientesListView(ListView):
    model=Cliente
    template_name='gestionClientes.html'
    
    def get_queryset(self):
        return Cliente.objects.all()
    def get_context_data(self, **kwargs):

        context= super().get_context_data(**kwargs)
        context['titulo']='Gestion Clientes'       
        return context
     
def eliminar_cliente(request,id):
    cliente= Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('/clientes/')

def registrar_cliente(request):
    cedula = request.POST['txtcedula']
    nombre= request.POST['txtname']
    apellido= request.POST['txtape']
    telefono= request.POST['txttel']
    direccion= request.POST['txtdir']
    cliente= Cliente.objects.create(Cedula=cedula,Nombre=nombre,Apellido=apellido,Telefono=telefono,Direccion=direccion)
    return redirect('/clientes/')

def edicion_cliente(request,id):
    cliente= Cliente.objects.get(id=id)
    data = {
        'titulo':'Edicion de Clientes',
        'clientes':cliente
    }
    return render(request,"edicionClientes.html",data)

def editar_cliente(request):
    id= int(request.POST['txtid'])
    nombre= request.POST['txtname']
    apellido= request.POST['txtape']
    telefono= request.POST['txttel']
    direccion= request.POST['txtdir']
    
    cliente= Cliente.objects.get(id=id)
    
    cliente.Nombre= nombre
    cliente.Apellido= apellido
    cliente.Telefono= telefono
    cliente.Direccion= direccion
    cliente.save()
    return redirect('/clientes/')

 

   