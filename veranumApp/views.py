from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from veranumApp.models import User, Habitacion
from django.contrib import messages
from django.core.mail import send_mail
from proyectoVeranum import settings

def loginPage(request):
    return render(request, "Login.html") 

def indexPage(request):
    return render(request, "Index.html")

def habitacionesPage(request):
    return render(request, "Habitaciones.html")

def listarPage(request):
    return render(request, "listar.html")


def autenticacion(request):
    username = request.POST['username']
    PASSWORD = request.POST['password']
    user = authenticate(request, username=username, password=PASSWORD)
    if user is not None:
        login(request, user)
        return render(request, "Index.html")
    else:
        return render(request, "Login.html")

def registrarse(request):
    nombre= request.POST['txt_nombre']
    apellido = request.POST['txt_apellido']
    rut = request.POST['txt_rut']
    sexo = request.POST['txt_sexo']
    pais = request.POST['txt_pais']
    ciudad = request.POST['txt_ciudad']
    direccion = request.POST['txt_direccion']
    correo = request.POST['txt_email']
    telefono = request.POST['txt_telefono']
    password = request.POST['txt_password']

    if len(nombre) and len(apellido) and len(rut) and len(sexo) and len(pais) and len(ciudad) and len(direccion) and len(correo) and len(telefono) and len(password):
        User.objects.create_user(username=correo, 
                                password=password, 
                                nombre = nombre,
                                apellido=apellido,
                                sexo= sexo,
                                pais=pais,
                                ciudad= ciudad,
                                direccion=direccion,
                                telefono=telefono,
                                rut = rut)
        messages.success(request, "Registrado correctamente")
        return render(request, "Login.html")
    else:
        messages.warning(request, "Up, no te has podido registrar")
        return render(request, "Login.html")

def cerrar_sesion(request):
    logout(request)
    return render(request, "Index.html")

def reservarHabitacion(request, tipo_habitacion):
    fecha_inicio = request.POST['txt_fecha_inicio']
    fecha_termino = request.POST['txt_fecha_termino']
    cantidad_personas = request.POST['txt_cantidad_personas']

    habitacion = Habitacion.objects.filter(tipo_Habitacion=tipo_habitacion)
    if habitacion:
        # modificar
        hab = Habitacion.objects.get(tipo_Habitacion=tipo_habitacion)
        hab.estado = False
        hab.fecha_inicio = fecha_inicio
        hab.fecha_termino = fecha_termino
        hab.cantidad_personas = cantidad_personas
        hab.save()

        # enviando correo

        if request.user.is_superuser != True:
            asunto = "RESERVA HOTELERA VERANUM"
            mensaje = "Su reservacion de la habitacion  " + tipo_habitacion + " del hotel Veranum, entre las fechas "+ fecha_inicio + " y " + fecha_termino + ", fue hecha correctamente."
            desde = settings.EMAIL_HOST_USER
            hacia = [request.user.username]
            fail_silently = False
            send_mail(asunto, mensaje, desde, hacia, fail_silently)


        messages.success(request, "Habitación reservada correctamente")
        return render(request, "Index.html")
    else:
        return render(request, "Habitaciones.html")
    #enviar email de confirmacion
    #send_mail('RESERVA HOTELERA', 'SU RESERVA FUE REALIZADA CORRECTAMENTE :)', 'Veranum.Hotel2021@gmail.com', [felipe.ariasv@gmail.com], fail_silently=False)

def verificar_disponibilidad(request, tipo_habitacion):
    habitacion = get_object_or_404(Habitacion, tipo_Habitacion = tipo_habitacion)
    if habitacion.estado:
        return render(request, "h"+tipo_habitacion+".html")
    else:
        messages.warning(request, "Habitacion en uso.")
        return render(request,"Habitaciones.html")

def listar(request):
    habitaciones = Habitacion.objects.all()
    data = {
        'habitaciones': habitaciones
    }
    return render(request,"listar.html",data)

def modificar(request, tipo_habitacion):    
    habitacion = Habitacion.objects.filter(tipo_Habitacion=tipo_habitacion)
    if habitacion:
        hab = Habitacion.objects.get(tipo_Habitacion=tipo_habitacion)
        hab.estado = True
        hab.save()
        messages.success(request, "Desocupado correctamente")
        return render(request, "listar.html")
    else:
        return render(request, "listar.html")

# correo veranum
# CORREO: Veranum.Hotel2021@gmail.com
# CONTRASENIA: veranum.Hotel2021