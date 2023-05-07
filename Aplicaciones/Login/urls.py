from django.urls import path,include
from Aplicaciones.Login.views import *

urlpatterns = [
    path('',home, name='home'),
    path('logout/',exit,name='exit'),

]

