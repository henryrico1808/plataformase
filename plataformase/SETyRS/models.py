from django.db import models
from django.contrib.auth.models import User
from login.models import CustomUser
from django.utils import timezone
from .validators import validate_file_extension

# Create your models here.

#--------------------------------------- Modelos de Institución ------------------------------------------------------------
# Tabla de las solicitudes de examenes a titulo
class SolicitudExamen(models.Model):
    oficio = models.CharField(max_length=20)
    cct = models.IntegerField()
    categoria = models.IntegerField()
    clave_institucion = models.IntegerField()
    institucion = models.CharField(max_length=50)
    area_carrera = models.CharField(max_length=30)
    id_presidente = models.IntegerField()
    id_secretario = models.IntegerField()
    id_vocal = models.IntegerField()
    estatus = models.IntegerField(default=1)
    fase = models.IntegerField(default=1)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fecha = models.DateField('fecha de publicacion')
    nivel_educativo = models.IntegerField(default=1)

    class Meta:
        db_table = 'SETyRS_solicitud_examen'

# Tabla de alumnos candidatos a graduarse registrados en las solicitudes de las instituciones
class Alumnos(models.Model):
    no_certificado = models.CharField(max_length=20)
    nombre_alumno = models.CharField(max_length=50)
    CURP = models.CharField(max_length=50)
    id_solicitud = models.ForeignKey(SolicitudExamen, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_alumno

    class Meta:
        db_table = 'SETyRS_alumnos'

# Tabla de las solicitudes de sinodales
class SolicitudSinodal(models.Model):
    estatus = models.IntegerField(default=1)
    institucion = models.CharField(max_length=50)
    fase = models.IntegerField(default=1)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fecha = models.DateField('fecha de publicacion')
    nivel_educativo = models.IntegerField(default=1)

    class Meta:
        db_table = 'SETyRS_solicitud_sinodal'

# Tabla de sinodales registrados por las instituciones
class Sinodales(models.Model):
    nombre_sinodal = models.CharField(max_length = 200)
    curp = models.CharField(max_length = 50)
    rfc = models.CharField(max_length = 50)
    grado_academico = models.CharField(max_length = 100)
    estatus = models.IntegerField(default=1)
    id_solicitud = models.ForeignKey(SolicitudSinodal, on_delete=models.CASCADE)
    nivel_educativo = models.IntegerField(default=1)
    institucion = models.CharField(max_length = 50, default='Instituto Tecnologico de Tepic')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_sinodal
    
    class Meta:
        db_table = 'SETyRS_sinodales'

# Tabla de documentos de los sinodales
class ArchivosSinodales(models.Model):
    sinodal = models.ForeignKey(Sinodales, on_delete=models.CASCADE)
    curriculum = models.FileField(upload_to='SETyRS/archivos/sinodales',validators=[validate_file_extension], blank=True, null=True)
    cedula = models.FileField(upload_to='SETyRS/archivos/sinodales',validators=[validate_file_extension], blank=True, null=True)
    solicitud = models.ForeignKey(SolicitudSinodal, on_delete=models.CASCADE)

    class Meta:
        db_table = 'SETyRS_documentos_sinodales'

# Tabla de notificaciones de las instituciones       
class Notificaciones(models.Model):
    descripcion = models.CharField(max_length=100)
    visto = models.BooleanField(default=False)
    fecha = models.DateTimeField('fecha de publicacion')
    solicitud_id = models.IntegerField()
    tipo_solicitud = models.IntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table = 'SETyRS_notificaciones_institucion'

# Tabla de documentos de los alumnos
class ArchivosAlumnos(models.Model):
    alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE)
    solicitud = models.ForeignKey(SolicitudExamen, on_delete=models.CASCADE)
    certificado_egreso = models.FileField(upload_to='SETyRS/archivos/alumnos',validators=[validate_file_extension], blank=True, null=True)
    servicio_social = models.FileField(upload_to='SETyRS/archivos/alumnos',validators=[validate_file_extension], blank=True, null=True)
    inscripcion_ctrl_escolar = models.FileField(upload_to='Archivos/Alumnos',validators=[validate_file_extension], blank=True, null=True)
    recibo_pago = models.FileField(upload_to='Archivos/Alumnos', validators=[validate_file_extension], blank=True, null=True)

    class Meta:
        db_table = 'SETyRS_documentos_alumnos'

#---------------------------------------- Modelos de administrador -------------------------------------------------------
# Tabla del historial de autorizacion de examenes a titulo
class Historial_admins_examen(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    solicitud = models.ForeignKey(SolicitudExamen, on_delete=models.CASCADE)
    fecha = models.DateField()
    comentarios = models.CharField(max_length=500, blank=True)
    estatus = models.BooleanField(default=False)
    departamento_id = models.IntegerField()

    class Meta:
        db_table = 'SETyRS_historial_examenes'

# Tabla del historial de autorizacion de sinodales
class Historial_admins_sinodal(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    sinodal = models.ForeignKey(Sinodales, on_delete=models.CASCADE)
    solicitud = models.ForeignKey(SolicitudSinodal, on_delete=models.CASCADE)
    fecha = models.DateField()
    comentarios = models.CharField(max_length=500, blank=True)
    estatus = models.BooleanField(default=False)
    departamento_id = models.IntegerField()

    class Meta:
        db_table = 'SETyRS_historial_sinodales'

#Tabla de notificaciones de administradores
class NotificacionAdmin(models.Model):
    descripcion = models.CharField(max_length=100)
    visto = models.BooleanField(default=False)
    fecha = models.DateTimeField('fecha de publicacion')
    solicitud_id = models.IntegerField()
    tipo_solicitud = models.IntegerField()
    departamento_id = models.IntegerField(default=1)

    class Meta:
        db_table = 'SETyRS_notificaciones_admin'
