"""proyectofinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tallermecanica import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
    path('home/', views.listadoclientes),
    path('listadoclientes/', views.listadoclientes),
    path('insertar/', views.insertar),
    path('eliminar/<int:ide>', views.eliminar),
    path('editar/<int:ide>', views.editar),
    path('listadovehiculos/', views.listadovehiculos),
    path('insertarvehiculo/', views.insertarvehiculo),
    path('eliminarvehiculo/<int:ide>', views.eliminarvehiculo),
    path('editarvehiculo/<int:ide>', views.editarvehiculo),
    path('listadoempleados/', views.listadoempleados),
    path('insertarempleado/', views.insertarempleado),
    path('eliminarempleado/<int:ide>', views.eliminarempleado),
    path('editarempleado/<int:ide>', views.editarempleado),
    path('asignarvehiculos/<int:id>', views.asignarvehiculos),
    path('listadoasignaciones/', views.listadoasignaciones),
    path('login/', views.login),
    path('cerrar/', views.cerrar),
]
