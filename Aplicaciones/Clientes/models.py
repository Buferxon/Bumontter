from django.db import models
from django.contrib.auth.models import Permission
# Create your models here.

# Create your models here.

class Cliente(models.Model):
    Cedula = models.BigIntegerField()
    Nombre=models.CharField(max_length=30)
    Apellido=models.CharField(max_length=30)
    Telefono=models.BigIntegerField()
    Direccion=models.CharField(max_length=30)
    Fecha_Registro = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.Nombre
    
    view_cliente = Permission.objects.get(codename='view_cliente')
    if not view_cliente:
        view_cliente = Permission.objects.create(
            codename='view_cliente',
            name='Can view cliente'
        )