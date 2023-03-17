from django.shortcuts import render,redirect
from .models import cliente,tipoidentificacion,ciudad,vehiculo,tipovehiculo,empleado,especialidad,asignarvehiculo,usuarios
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'index.html')


def listadoclientes(request):
    datos=cliente.objects.all
    return render(request,'clientes/listar.html',{'datos':datos})

def eliminar(request,ide):
    data=cliente.objects.get(id=ide)
    data.delete()
    return redirect("/listadoclientes/")


def insertar(request):
    if request.POST:
        ciudadcliente=ciudad.objects.get(id=request.POST["idciudad"])
        tipoidcliente=tipoidentificacion.objects.get(id=request.POST["idtipoidentificacion"])
        nuevo=cliente(
            idtipoidentificacion=tipoidcliente,
            cedula=request.POST["cedula"],
            nombre=request.POST["nombre"],
            apellido=request.POST["apellido"],
            telefono=request.POST["telefono"],
            direccion=request.POST["direccion"],
            idciudad=ciudadcliente,
            correo=request.POST["correo"]
        )
        nuevo.save()
        return redirect("/listadoclientes/")
    datos=tipoidentificacion.objects.all
    ciudades=ciudad.objects.all
    return render(request,'clientes/insertar.html',{'datos':datos,'ciudades':ciudades})

def editar(request,ide):
    edicioncliente=cliente.objects.get(id=ide)
    if request.POST:
        ciudadcliente=ciudad.objects.get(id=request.POST["idciudad"])
        tipoidcliente=tipoidentificacion.objects.get(id=request.POST["idtipoidentificacion"])
        edicioncliente=cliente.objects.filter(id=ide).update(
            idtipoidentificacion=tipoidcliente,
            cedula=request.POST["cedula"],
            nombre=request.POST["nombre"],
            apellido=request.POST["apellido"],
            telefono=request.POST["telefono"],
            direccion=request.POST["direccion"],
            idciudad=ciudadcliente,
            correo=request.POST["correo"]
        )
        return redirect("/listadoclientes/")
    datos=tipoidentificacion.objects.all
    ciudades=ciudad.objects.all
    return render(request,'clientes/editar.html',{'clienteeditar':edicioncliente,'datos':datos,'ciudades':ciudades})    


def listadovehiculos(request):
    datos=vehiculo.objects.all
    return render(request,'vehiculos/listar.html',{'datos':datos})

def eliminarvehiculo(request,ide):
    data=vehiculo.objects.get(id=ide)
    data.delete()
    return redirect("/listadovehiculos/")


def insertarvehiculo(request):
    print(request)
    if request.POST:
        ciudadvehiculo=ciudad.objects.get(id=request.POST["idciudad"])
        clientevehiculo=cliente.objects.get(cedula=request.POST["cedula"])
        tipoidvehiculo=tipovehiculo.objects.get(id=request.POST["idtipovehiculo"])
        nuevo=vehiculo(
            placa=request.POST["placa"],
            modelo=request.POST["modelo"],
            marca=request.POST["marca"],
            cedula=clientevehiculo,    
            idciudad=ciudadvehiculo,
            idtipovehiculo=tipoidvehiculo
        )
        nuevo.save()
        return redirect("/listadovehiculos/")
    datos=tipovehiculo.objects.all
    ciudades=ciudad.objects.all
    return render(request,'vehiculos/insertar.html',{'datos':datos,'ciudades':ciudades})


def editarvehiculo(request,ide):
    edicionvehiculo=vehiculo.objects.get(id=ide)
    if request.POST:
        ciudadvehiculo=ciudad.objects.get(id=request.POST["idciudad"])
        tipoidvehiculo=tipovehiculo.objects.get(id=request.POST["idtipovehiculo"])
        clientevehiculo=cliente.objects.get(cedula=request.POST["cedula"])
        edicionvehiculo=vehiculo.objects.filter(id=ide).update(
            placa=request.POST["placa"],
            modelo=request.POST["modelo"],
            marca=request.POST["marca"],
            cedula=clientevehiculo,    
            idciudad=ciudadvehiculo,
            idtipovehiculo=tipoidvehiculo
        )
        return redirect("/listadovehiculos/")
    datos=tipovehiculo.objects.all
    ciudades=ciudad.objects.all
    return render(request,'vehiculos/editar.html',{'vehiculoeditar':edicionvehiculo,'datos':datos,'ciudades':ciudades})    


def listadoempleados(request):
    datos=empleado.objects.all
    return render(request,'empleados/listar.html',{'datos':datos})

def eliminarempleado(request,ide):
    data=empleado.objects.get(id=ide)
    data.delete()
    return redirect("/listadoempleados/")

def insertarempleado(request):
    print(request)
    if request.POST:
        ciudadempleado=ciudad.objects.get(id=request.POST["idciudad"])
        tipoidentificacionempleado=tipoidentificacion.objects.get(id=request.POST["idtipoidentificacion"])
        tipoespecialidad=especialidad.objects.get(id=request.POST["idespecialidad"])
        nuevo=empleado(
            idtipoidentificacion=tipoidentificacionempleado,
            cedula=request.POST["cedula"],
            nombre=request.POST["nombre"],
            apellido=request.POST["apellido"],
            telefono=request.POST["telefono"],
            direccion=request.POST["direccion"],
            idciudad=ciudadempleado,
            correo=request.POST["correo"],
            idespecialidad=tipoespecialidad
        )
        nuevo.save()
        return redirect("/listadoempleados/")
    ciudades=ciudad.objects.all
    especialidades=especialidad.objects.all
    datos=tipoidentificacion.objects.all
    return render(request,'empleados/insertar.html',{'datos':datos,'ciudades':ciudades,"especialidades":especialidades})


def editarempleado(request,ide):
    editarempleados=empleado.objects.get(id=ide)
    if request.POST:
        ciudadempleado=ciudad.objects.get(id=request.POST["idciudad"])
        tipoidentificacionempleado=tipoidentificacion.objects.get(id=request.POST["idtipoidentificacion"])
        tipoespecialidad=especialidad.objects.get(id=request.POST["idespecialidad"])
        editarempleado=empleado.objects.filter(id=ide).update(
            idtipoidentificacion=tipoidentificacionempleado,
            cedula=request.POST["cedula"],
            nombre=request.POST["nombre"],
            apellido=request.POST["apellido"],
            telefono=request.POST["telefono"],
            direccion=request.POST["direccion"],
            idciudad=ciudadempleado,
            correo=request.POST["correo"],
            idespecialidad=tipoespecialidad
        )
        return redirect("/listadoempleados/")
    ciudades=ciudad.objects.all
    especialidades=especialidad.objects.all
    datos=tipoidentificacion.objects.all
    return render(request,'empleados/editar.html',{'empleadoeditar':editarempleados,"datos":datos,'ciudades':ciudades,"especialidades":especialidades})

def asignarvehiculos(request,id):
    empleadoasignar=empleado.objects.get(id=id)
    
    if request.POST:
        vehiculoelejido=vehiculo.objects.get(id=request.POST["vehiculoasignado"])
        nuevo=asignarvehiculo(
            vehiculoasignado=vehiculoelejido,
            empleadovehiculo=empleadoasignar
        )
        nuevo.save()    
        return redirect("/listadoasignaciones/")
    vehiculos=vehiculo.objects.all
    return render(request,'asignarvehiculos/insertar.html',{"vehiculos":vehiculos,"empleado":empleadoasignar})


def listadoasignaciones(request):
    asignaciones=asignarvehiculo.objects.all
    if request.POST:
        vehiculoelejido=vehiculo.objects.get(id=request.POST["vehiculoasignado"])
        vehiculoasignado=vehiculoelejido
        return redirect("/listadoasignaciones/")
    return render(request,'asignarvehiculos/listar.html',{"asignaciones":asignaciones})    

def carrusel(request):
    return render(request,"paginas/carrusel.html")

def login(request):
    if request.POST:
        logear=usuarios.objects.filter(usuario=request.POST["usuario"],clave=request.POST["contrasena"])
        if logear.count()!=0:
          return redirect("/home/")  
    return render(request,"registro/login.html")

def cerrar(request):
    return redirect("/login/")