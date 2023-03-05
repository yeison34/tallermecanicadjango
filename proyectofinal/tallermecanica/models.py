from django.db import models
from datetime import datetime
class ciudad(models.Model):
    id=models.AutoField(primary_key=True)
    codigo=models.CharField(max_length=10)
    nombre=models.CharField(max_length=300)
    
class tipoidentificacion(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=300)

class cliente(models.Model):
    id=models.AutoField(primary_key=True)
    idtipoidentificacion=models.ForeignKey(tipoidentificacion,on_delete=models.CASCADE)
    cedula=models.CharField(max_length=12)
    nombre=models.CharField(max_length=300)
    apellido=models.CharField(max_length=300)
    telefono=models.CharField(max_length=12)
    correo=models.CharField(max_length=300)
    direccion=models.CharField(max_length=300)
    idciudad=models.ForeignKey(ciudad,on_delete=models.CASCADE)
    
class tipovehiculo(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=300)

class vehiculo(models.Model):
    id=models.AutoField(primary_key=True)
    placa=models.CharField(max_length=10)
    modelo=models.CharField(max_length=40)
    marca=models.CharField(max_length=100)
    cedula=models.ForeignKey(cliente,on_delete=models.CASCADE)    
    idciudad=models.ForeignKey(ciudad,on_delete=models.CASCADE)
    idtipovehiculo=models.ForeignKey(tipovehiculo,on_delete=models.CASCADE) 
    
class especialidad(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=300)
    sueldo=models.CharField(max_length=300)
    
class empleado(models.Model):
    id=models.AutoField(primary_key=True)
    idtipoidentificacion=models.ForeignKey(tipoidentificacion,on_delete=models.CASCADE)
    cedula=models.CharField(max_length=12)
    nombre=models.CharField(max_length=300)
    apellido=models.CharField(max_length=300)
    telefono=models.CharField(max_length=12)
    correo=models.CharField(max_length=300)
    direccion=models.CharField(max_length=300)
    idciudad=models.ForeignKey(ciudad,on_delete=models.CASCADE)
    idespecialidad=models.ForeignKey(especialidad,on_delete=models.CASCADE)
    fechaingreso=models.DateField(default=datetime.now())
    
class asignarvehiculo(models.Model):
    id=models.AutoField(primary_key=True)
    empleadovehiculo=models.ForeignKey(empleado,on_delete=models.CASCADE,null=True) 
    vehiculoasignado=models.ForeignKey(vehiculo,on_delete=models.CASCADE)    
    fechasignacion=models.DateField(default=datetime.now())