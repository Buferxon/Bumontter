from django.contrib import admin
from .models import Cliente
# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display=('id','Cedula','Nombre','Apellido','Telefono','Direccion','Fecha_Registro')
    # search_fields=('Cedula',)
    
    
    """
    fieldsets=(
        (None,{
            'fields':('Nombre',)
        }),
        ('Advanced options',{
            'classes':('collapse','wide','extrapretty'),
            'fields':('Cedula',)
        })
    )
    """

# admin.site.register(Cliente)

# admin.site.register(Cliente,ClienteAdmin)
