# Generated by Django 2.2.1 on 2020-06-25 23:49

import SETyRS.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_certificado', models.CharField(max_length=20)),
                ('nombre_alumno', models.CharField(max_length=50)),
                ('CURP', models.CharField(max_length=50)),
                ('folio_pago', models.CharField(blank=True, default='1234', max_length=50)),
                ('carrera', models.CharField(blank=True, default='Carrera', max_length=100)),
            ],
            options={
                'db_table': 'SETyRS_alumnos',
            },
        ),
        migrations.CreateModel(
            name='ArchivosAlumnos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificado_egreso', models.FileField(blank=True, null=True, upload_to='SETyRS/archivos/alumnos', validators=[SETyRS.validators.validate_file_extension])),
                ('servicio_social', models.FileField(blank=True, null=True, upload_to='SETyRS/archivos/alumnos', validators=[SETyRS.validators.validate_file_extension])),
                ('inscripcion_ctrl_escolar', models.FileField(blank=True, null=True, upload_to='SETyRS/archivos/alumnos', validators=[SETyRS.validators.validate_file_extension])),
                ('recibo_pago', models.FileField(blank=True, null=True, upload_to='SETyRS/archivos/alumnos', validators=[SETyRS.validators.validate_file_extension])),
                ('comprobante_exp', models.FileField(blank=True, null=True, upload_to='SETyRS/archivos/alumnos', validators=[SETyRS.validators.validate_file_extension])),
            ],
            options={
                'db_table': 'SETyRS_documentos_alumnos',
            },
        ),
        migrations.CreateModel(
            name='ArchivosSinodales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curriculum', models.FileField(blank=True, null=True, upload_to='SETyRS/archivos/sinodales', validators=[SETyRS.validators.validate_file_extension])),
                ('cedula', models.FileField(blank=True, null=True, upload_to='SETyRS/archivos/sinodales', validators=[SETyRS.validators.validate_file_extension])),
            ],
            options={
                'db_table': 'SETyRS_documentos_sinodales',
            },
        ),
        migrations.CreateModel(
            name='Historial_admins_examen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('comentarios', models.CharField(blank=True, max_length=500)),
                ('estatus', models.BooleanField(default=False)),
                ('nivel_educativo', models.IntegerField()),
            ],
            options={
                'db_table': 'SETyRS_historial_examenes',
            },
        ),
        migrations.CreateModel(
            name='Historial_admins_sinodal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('comentarios', models.CharField(blank=True, max_length=500)),
                ('estatus', models.BooleanField(default=False)),
                ('nivel_educativo', models.IntegerField()),
            ],
            options={
                'db_table': 'SETyRS_historial_sinodales',
            },
        ),
        migrations.CreateModel(
            name='NotificacionAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('visto', models.BooleanField(default=False)),
                ('fecha', models.DateTimeField(verbose_name='fecha de publicacion')),
                ('solicitud_id', models.IntegerField()),
                ('tipo_solicitud', models.IntegerField()),
                ('nivel_educativo', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'SETyRS_notificaciones_admin',
            },
        ),
        migrations.CreateModel(
            name='Notificaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('visto', models.BooleanField(default=False)),
                ('fecha', models.DateTimeField(verbose_name='fecha de publicacion')),
                ('solicitud_id', models.IntegerField()),
                ('tipo_solicitud', models.IntegerField()),
            ],
            options={
                'db_table': 'SETyRS_notificaciones_institucion',
            },
        ),
        migrations.CreateModel(
            name='Sinodales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_sinodal', models.CharField(max_length=200)),
                ('curp', models.CharField(max_length=50)),
                ('rfc', models.CharField(max_length=50)),
                ('grado_academico', models.CharField(max_length=100)),
                ('estatus', models.IntegerField(default=1)),
                ('nivel_educativo', models.IntegerField(default=1)),
                ('institucion', models.CharField(default='Instituto Tecnologico de Tepic', max_length=50)),
            ],
            options={
                'db_table': 'SETyRS_sinodales',
            },
        ),
        migrations.CreateModel(
            name='SolicitudExamen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.IntegerField()),
                ('institucion', models.IntegerField(default=1)),
                ('area_carrera', models.CharField(blank=True, max_length=30)),
                ('id_presidente', models.IntegerField()),
                ('id_secretario', models.IntegerField()),
                ('id_vocal', models.IntegerField()),
                ('estatus', models.IntegerField(default=1)),
                ('fase', models.IntegerField(default=1)),
                ('fecha', models.DateField(verbose_name='fecha de publicacion')),
                ('nivel_educativo', models.IntegerField(default=1)),
                ('fecha_exa', models.DateField(default='2020-06-06')),
                ('lugar_exa', models.CharField(default='Algun lugar', max_length=50)),
            ],
            options={
                'db_table': 'SETyRS_solicitud_examen',
            },
        ),
        migrations.CreateModel(
            name='SolicitudSinodal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estatus', models.IntegerField(default=1)),
                ('institucion', models.CharField(max_length=50)),
                ('fase', models.IntegerField(default=1)),
                ('fecha', models.DateField(verbose_name='fecha de publicacion')),
                ('nivel_educativo', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'SETyRS_solicitud_sinodal',
            },
        ),
    ]
