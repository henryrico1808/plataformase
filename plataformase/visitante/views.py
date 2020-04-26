from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from RVOES.models import Departamento
from login.models import CustomUser
from RVOES.models import NotificacionRegistro
from .models import VisitanteSC,ConfiguracionPDF
from django.contrib.auth.hashers import make_password

''' Vistas que redireccionan respecto a permisos de usuario'''
def index(request):
    return render(request,'registration/login.html')

def menuinstitucion(request):
    return render(request,'menuinstitucion.html')

def menuparticular(request):
    return render(request,'menuparticular.html')

def menuadmin(request):
    NumSolicitudes = VisitanteSC.objects.filter(leida='0').count()
    if NumSolicitudes>0:
       return render(request, 'menuadmin.html', {"numSol": NumSolicitudes})
    else:
        return render(request,'menuadmin.html')

def menudepartamento(request):
    return render(request,'menudepartamento.html')

def control(request):
    return render(request,'menudepartamento_ce.html')

def menuvisitante(request):
    return render(request,'menuvisitante.html')

def cuentavisitante(request):
    return render(request,'cuentavisitante.html')

'''Función que muestra los datos de los formatos de pdf existentes.'''
def configuracionpdf(request):
    formatos = ConfiguracionPDF.objects.all()
    return render(request, 'configuracionpdf.html', {'formatos': formatos })

'''perfiluser, muestra los datos del usuario que este logueado'''
def perfiluser(request):
 
    if request.user.tipo_usuario=='1' and request.user.tipo_persona=='1':
        return render(request,'perfiluserIF.html')
    else:
        if request.user.tipo_usuario=='1' and request.user.tipo_persona=='2':
            return render(request,'perfiluserIM.html')
    
        if request.user.tipo_persona=='1':
            return render(request,'perfiluser.html')
        else:
            return render(request,'perfiluserMoral.html')

def visit(request):
    try:
        #Obtenemos el primer elemento de los departamentos.
        dep = Departamento.objects.get(id=1)
    except Departamento.DoesNotExist:
        #Si no existe un departamento, entonces los insertamos en la base de datos.
        a = Departamento(id=1, nombre='Control Escolar')
        a.save()
        b = Departamento(id=2, nombre='Dirección')
        b.save()
        c = Departamento(id=3, nombre='Superior')
        c.save()
        d = Departamento(id=4, nombre='Media Superior')
        d.save()
    if Departamento.objects.get(id=3)=="Superior":
         return redirect('cuentavisitante')

def notificacion(request):
    if request.method == 'POST':
        import datetime
        cad=request.POST["email"]+" ,"+request.POST["tipo_usuario"]+","+request.POST["first_name"]+" "+request.POST["last_name"]+" ,"+request.POST["celular"]+", "+request.POST["curp_rfc"]
        notificacionUsr = NotificacionRegistro(
                                        email=request.POST["email"],
                                        curp=request.POST["curp_rfc"],
                                        nombres=request.POST["first_name"]+" "+request.POST["last_name"],
                                        leida='0',
                                        celular=request.POST["celular"],
                                        tipo_usuario=request.POST["tipo_usuario"],
                                        fechaNotificacion=datetime.datetime.now(),
                                        tipo_notificacion='R',
                                        usuario_id=1)
        notificacionUsr.save()
        return render(request,'menuvisitante.html')
def notificacionadmon(request):
    """Muestra al usuario las notificaciones que tiene como no leídas.

    Parámetros
    -:param request: Contiene información del navegador del usuario que está realizando la petición.

    Retorna
    -:return: Regresa la vista en la cual el usuario podrá revisar las notificaciones que tiene que no han sido leídas.
    """
    if request.user.tipo_usuario == '4':
        import pickle # Importa una librería que nos permite la manipulación del acceso a memoria de una manera mas directa.
        NotificacionR = NotificacionRegistro.objects.filter(leida='0', tipo_notificacion='R', usuario_id=request.user.id).order_by(
            'fechaNotificacion')# Se obtienen todas las notificaciones no leídas (leida=0) de tipo 'Historial'(H) del usuario en sesión.
        s = pickle.dumps(NotificacionR)#Ponemos en memoria lo almacenado en 'Notificaciones' y almacenamos en 's' la referencia a estos datos.
        NotificacionRegistro.objects.filter(usuario_id=request.user.id, leida='0').update(leida='1')# Actualizamos las notificaciones no leídas del usuario, de "leida='0'" a "leida='1'", lo que se interpreta como que las mismas ya fueron leídas.
        NotificacionesAuxiliar = pickle.loads(s)# Almacenamos en 'NotificacionesAuxiliar' lo referenciado por 's'.
        return render(request, 'notificacionadmon.html', {"notificaciones": NotificacionesAuxiliar})
    else:
        return redirect('perfil')

#Registra al visitante como una solicitu
def regVisit(request):
    if request.method == 'POST':
        import datetime
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        curp_rfc = request.POST["curp_rfc"]
        calle = request.POST["calle"]
        password = request.POST["password"]
        noexterior = request.POST["noexterior"]
        nointerior = request.POST["nointerior"]
        codigopostal = request.POST["codigopostal"]
        municipio = request.POST["municipio"]
        colonia = request.POST["colonia"]
        celular = request.POST["celular"]
        tipo_usuario = request.POST["tipo_usuario"]
        tipo_persona = request.POST["tipo_persona"]
        departamento = int(request.POST["departamento"])
        if tipo_usuario == '2':
            jefe = '1'
        else:
            jefe = '0'
                #Si el tipo de usuario es institución(1) o administrador del sistema(4)
        if tipo_usuario == '1' or tipo_usuario == '4' or tipo_usuario == '5':
            departamento = None
        if VisitanteSC.objects.filter(jefe='1', departamento_id=departamento).exists():
            VisitanteSC.objects.filter(jefe='1', departamento_id=departamento).update(jefe='0')
        visit = VisitanteSC(first_name=first_name,last_name=last_name, password="se2020",email=email, curp_rfc=curp_rfc, calle=calle,
                            noexterior=noexterior, nointerior=nointerior, codigopostal=codigopostal,
                            municipio=municipio, colonia=colonia, celular=celular, tipo_usuario=tipo_usuario,
                            tipo_persona=tipo_persona,
                            departamento_id=departamento, jefe=jefe)
        visit.save()
        return redirect('solicitudenviada') #mandar pagina con mensaje de esperar
    # else:
    #     return redirect('solicitudcuenta')

def modal(request):
    return render(request,'modal.html')

#notificasiones solicitud de cuenta, muestra las nuevas solicitudes de cuenta al administrador
def notificacionsc(request):
    visitantes = VisitanteSC.objects.filter(leida='0')
    return render(request, 'notificacionsc.html', {'visitantes': visitantes })

#Funcion que manda los datos del visitante que pidió cuenta, se valida y puede aceptarse o no.
def validar(request,email):
    vs=VisitanteSC.objects.get(email = email)
    return render(request,'validar.html',{'VisitanteSC':vs})


def regUser(request):
    """Registra a los usuarios en la base de datos.

    Parámetros
    -:param request: Contiene información del navegador del usuario esta realizando la petición.

    Retorna
    -:return redirect 'root': Regresa a la pantalla principal del administrador del sistema.
    -:return redirect 'signup': Regresa la vista en la cual el usuario podrá añadir nuevos usuarios.
    """
    if request.user.tipo_usuario == '4':
        if request.method == 'POST':
            import datetime
            #Generamos las variables con los datos recibidos del request.
            username = request.POST["email"]
            curp_rfc = request.POST["curp_rfc"]
            calle = request.POST["calle"]
            password = make_password(request.POST["password2"])
            noexterior = request.POST["noexterior"]
            nointerior = request.POST["nointerior"]
            codigopostal = request.POST["codigopostal"]
            municipio = request.POST["municipio"]
            colonia = request.POST["colonia"]
            celular = request.POST["celular"]
            tipo_usuario = request.POST["tipo_usuario"]
            tipo_persona = request.POST["tipo_persona"]
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            if tipo_usuario!='2':
                firma_digital=request.POST["first_name"]
            else:
                firma_digital = request.FILES["firma_digital"]
            if tipo_usuario!= '1' and tipo_usuario!='4' and tipo_usuario!='5':
                departamento = int(request.POST["departamento"])

    
            #Sí el usuario es jefe de departamento (tipo_usuario:2)
            if tipo_usuario == '2':
                #Definimos jefe como 1 (sí es jefe de departamento)
                jefe = '1'
            else:
                #Definimos jefe como 0 (no es jefe de departamento)
                jefe = '0'
                firma_digital= None
               
                #Si el tipo de usuario es institución(1) o administrador del sistema(4)
                if tipo_usuario == '1' or tipo_usuario == '4' or tipo_usuario=='5':
                    firma_digital= None
                    #Aseguramos que no pertenezcan a ningún departamento
                    departamento = None
            #Obtenemos el ID del usuario que registro a al nuevo usuario
            registro = (request.user.id)
            #Si existe un usuario que sea jefe de ese departamento
            if CustomUser.objects.filter(jefe='1', departamento_id=departamento).exists():
                #Se le hace usuario normal
                CustomUser.objects.filter(jefe='1', departamento_id=departamento).update(jefe='0')
            #Registramos el usuario en la base de datos
            usr = CustomUser(username=username, password=password, curp_rfc=curp_rfc, calle=calle,
                            noexterior=noexterior, nointerior=nointerior, codigopostal=codigopostal,
                            municipio=municipio, colonia=colonia, celular=celular, tipo_usuario=tipo_usuario,
                            tipo_persona=tipo_persona, first_name=first_name, last_name=last_name,
                            departamento_id=departamento, jefe=jefe, registro_id=registro,
                            date_joined=datetime.datetime.now(),firma_digital=firma_digital)
            usr.save()
            VisitanteSC.objects.filter(email=username,leida='0').update(leida='1') #email=email en caso de que ya vuelva el email en lugar de user
            return redirect('usuarios')
        else:
            return redirect('signup')
    else:
        return redirect('perfil')
         

def cancelarsolicitud(request,email2,email):
    # vs=VisitanteSC.objects.get(email = email2)
    VisitanteSC.objects.filter(email=email2,leida='0').update(leida='1')
    return redirect('notificacionsc')

#Actualizar datos de los usuarios
def actualizarperfilusr(request):

    if request.method == 'POST':
        first_name = request.POST["first_name"]
        if request.user.tipo_persona=='1':
            last_name = request.POST["last_name"]
        else:
            last_name=""
        email = request.POST["email"]
        curp_rfc = request.POST["curp_rfc"]
        calle = request.POST["calle"]
        #password = make_password(request.POST["password2"])
        noexterior = request.POST["noexterior"]
        nointerior = request.POST["nointerior"]
        codigopostal = request.POST["codigopostal"]
        municipio = request.POST["municipio"]
        colonia = request.POST["colonia"]
        celular = request.POST["celular"]
        if request.user.tipo_usuario=='1':
            inst_cct=request.POST["cct"]
            inst_nombredirector=request.POST["nombre_director"]

        else:
            inst_cct=None
            inst_nombredirector=None

        
        CustomUser.objects.filter(email=email).update(curp_rfc=curp_rfc,calle=calle,noexterior=noexterior,nointerior=nointerior,
        codigopostal=codigopostal,municipio=municipio,colonia=colonia,celular=celular,first_name=first_name,last_name=last_name,
        inst_cct=inst_cct,inst_nombredirector=inst_nombredirector)
        return redirect('perfiluser') 


def GuardarFormatoPDF(request):
    if request.method == 'POST':
        nombre = request.POST["nombre"]
        descripcion = request.POST["descripcion"]
        fondo = request.FILES["fondo"]
        formatoPDF= ConfiguracionPDF(nombre=nombre,descripcion=descripcion,fondo=fondo)
        formatoPDF.save()
        formatos = ConfiguracionPDF.objects.all()
        return render(request, 'configuracionpdf.html', {'formatos': formatos })
     


