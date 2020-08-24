# Generated by Django 2.2.1 on 2020-08-24 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInteres',
            fields=[
                ('Clave_Area', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('Clave_Carrera', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre_Carrera', models.CharField(max_length=50)),
                ('areaInteres', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SigApp.AreaInteres')),
            ],
        ),
        migrations.CreateModel(
            name='CentroTrabajo',
            fields=[
                ('Clave_CentroTrabajo', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Nombre_CentroTrabajo', models.CharField(max_length=100)),
                ('Descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DatosTemporal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave_centrotrabajo_temp', models.CharField(max_length=200)),
                ('direccion_temp', models.CharField(max_length=200)),
                ('director_temp', models.CharField(max_length=200)),
                ('nombre_institucion', models.CharField(max_length=200)),
                ('municipio', models.CharField(max_length=200)),
                ('localidad', models.CharField(max_length=200)),
                ('usuario_mod', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(max_length=200)),
                ('latitud_temp', models.CharField(max_length=200, null=True)),
                ('longitud_temp', models.CharField(max_length=200, null=True)),
                ('modificando', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='DatosTemporalEstadistica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClaveEscuela_temp', models.CharField(max_length=200)),
                ('NombreCarrera_temp', models.CharField(max_length=200)),
                ('TotalPrimero_temp', models.IntegerField()),
                ('TotalSegundo_temp', models.IntegerField()),
                ('TotalTercero_temp', models.IntegerField()),
                ('TotalCuarto_temp', models.IntegerField()),
                ('TotalQuinto_temp', models.IntegerField()),
                ('TotalSexto_temp', models.IntegerField()),
                ('TotalHombres_temp', models.IntegerField()),
                ('TotalMujeres_temp', models.IntegerField()),
                ('Tipo_temp', models.CharField(max_length=50)),
                ('Area_temp', models.CharField(blank=True, max_length=100, null=True)),
                ('ClaveCarrera_temp', models.CharField(max_length=30)),
                ('Modalidad_temp', models.CharField(max_length=25)),
                ('Periodos_temp', models.CharField(max_length=25)),
                ('usuario_mod', models.CharField(blank=True, max_length=50, null=True)),
                ('modificando', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('IdEscuela', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('NombreEscuela', models.CharField(max_length=50)),
                ('RazonSocial', models.CharField(max_length=50)),
                ('Dominio', models.CharField(max_length=50)),
                ('Personal', models.CharField(max_length=50)),
                ('CodPostal', models.CharField(max_length=50)),
                ('ClaveM', models.CharField(max_length=50)),
                ('Municipio', models.CharField(max_length=50)),
                ('ClaveL', models.CharField(max_length=50)),
                ('Localidad', models.CharField(max_length=50)),
                ('Latitud', models.CharField(max_length=50)),
                ('Longitud', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EscuelaC',
            fields=[
                ('ClaveEscuela', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('NombreEscuela', models.CharField(max_length=200)),
                ('EstatusEscuela', models.CharField(max_length=200)),
                ('Calle', models.CharField(max_length=200)),
                ('Municipio', models.CharField(max_length=200)),
                ('Localidad', models.CharField(max_length=200)),
                ('CodPostal', models.CharField(max_length=200)),
                ('Latitud', models.CharField(max_length=200)),
                ('Longitud', models.CharField(max_length=200)),
                ('Dominio', models.CharField(max_length=200)),
                ('nombreDirector', models.CharField(max_length=200)),
                ('ApellidoP_Director', models.CharField(max_length=200)),
                ('ApellidoM_Director', models.CharField(max_length=200)),
                ('Telefono_Director', models.CharField(max_length=200)),
                ('Celuar_Director', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200)),
                ('Nivel', models.CharField(max_length=200)),
                ('TipoServicio', models.CharField(max_length=200)),
                ('ImagenNo1', models.ImageField(blank=True, null=True, upload_to='imagenes_instituciones_perfil')),
                ('ImagenNo2', models.ImageField(blank=True, null=True, upload_to='imagenes_instituciones_perfil')),
                ('ImagenNo3', models.ImageField(blank=True, null=True, upload_to='imagenes_instituciones_perfil')),
            ],
        ),
        migrations.CreateModel(
            name='GradoAcademico',
            fields=[
                ('Clave_GradoAcademico', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='HistorialMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechamod', models.DateTimeField()),
                ('departamento', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_dep', models.CharField(max_length=200)),
                ('usuario_mod', models.CharField(max_length=200)),
                ('tipo', models.BooleanField(blank=True, null=True)),
                ('comentario', models.CharField(blank=True, max_length=500, null=True)),
                ('clave_centrotrabajo_prev', models.CharField(max_length=200)),
                ('direccion_prev', models.CharField(max_length=200)),
                ('director_prev', models.CharField(max_length=200)),
                ('nombre_institucion_prev', models.CharField(max_length=200)),
                ('municipio_prev', models.CharField(max_length=200)),
                ('localidad_prev', models.CharField(max_length=200)),
                ('latitud_prev', models.CharField(max_length=200, null=True)),
                ('longitud_prev', models.CharField(max_length=200, null=True)),
                ('status_prev', models.CharField(max_length=200)),
                ('clave_centrotrabajo_new', models.CharField(max_length=200)),
                ('direccion_new', models.CharField(max_length=200)),
                ('director_new', models.CharField(max_length=200)),
                ('nombre_institucion_new', models.CharField(max_length=200)),
                ('municipio_new', models.CharField(max_length=200)),
                ('localidad_new', models.CharField(max_length=200)),
                ('latitud_new', models.CharField(max_length=200, null=True)),
                ('longitud_new', models.CharField(max_length=200, null=True)),
                ('status_new', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HistorialModEstadistica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechamod', models.DateTimeField()),
                ('tipo', models.BooleanField(blank=True, null=True)),
                ('comentario', models.CharField(blank=True, max_length=500, null=True)),
                ('usuario_dep', models.CharField(max_length=200)),
                ('usuario_mod', models.CharField(max_length=200)),
                ('departamento', models.CharField(blank=True, max_length=50, null=True)),
                ('ClaveEscuela_prev', models.CharField(max_length=200)),
                ('ClaveCarrera_prev', models.CharField(max_length=30)),
                ('NombreCarrera_prev', models.CharField(max_length=200)),
                ('TotalAlumnos_prev', models.IntegerField(blank=True, null=True)),
                ('TotalPrimero_prev', models.IntegerField()),
                ('TotalSegundo_prev', models.IntegerField()),
                ('TotalTercero_prev', models.IntegerField()),
                ('TotalCuarto_prev', models.IntegerField()),
                ('TotalQuinto_prev', models.IntegerField()),
                ('TotalSexto_prev', models.IntegerField()),
                ('TotalHombres_prev', models.IntegerField()),
                ('TotalMujeres_prev', models.IntegerField()),
                ('Tipo_prev', models.CharField(max_length=50)),
                ('Area_prev', models.CharField(blank=True, max_length=100, null=True)),
                ('Modalidad_prev', models.CharField(max_length=25)),
                ('Periodos_prev', models.CharField(max_length=25)),
                ('ClaveEscuela_new', models.CharField(max_length=200)),
                ('ClaveCarrera_new', models.CharField(max_length=30)),
                ('NombreCarrera_new', models.CharField(max_length=200)),
                ('TotalAlumnos_new', models.IntegerField(blank=True, null=True)),
                ('TotalPrimero_new', models.IntegerField()),
                ('TotalSegundo_new', models.IntegerField()),
                ('TotalTercero_new', models.IntegerField()),
                ('TotalCuarto_new', models.IntegerField()),
                ('TotalQuinto_new', models.IntegerField()),
                ('TotalSexto_new', models.IntegerField()),
                ('TotalHombres_new', models.IntegerField()),
                ('TotalMujeres_new', models.IntegerField()),
                ('Tipo_new', models.CharField(max_length=50)),
                ('Area_new', models.CharField(blank=True, max_length=100, null=True)),
                ('Modalidad_new', models.CharField(max_length=25)),
                ('Periodos_new', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('Clave_Institucion', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Nombre_Institucion', models.CharField(max_length=100)),
                ('estatus', models.CharField(max_length=15)),
                ('Dominio_Institucion', models.CharField(max_length=7)),
                ('totalDocentes', models.BigIntegerField()),
                ('totalAdministrativos', models.BigIntegerField()),
                ('Director_Institucion', models.CharField(max_length=100)),
                ('ImagenNo1', models.ImageField(blank=True, null=True, upload_to='imagenes_instituciones_perfil')),
                ('ImagenNo2', models.ImageField(blank=True, null=True, upload_to='imagenes_instituciones_perfil')),
                ('ImagenNo3', models.ImageField(blank=True, null=True, upload_to='imagenes_instituciones_perfil')),
                ('Clave_CentroTrabajo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SigApp.CentroTrabajo')),
            ],
        ),
        migrations.CreateModel(
            name='Modalidad',
            fields=[
                ('Clave_Modalidad', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('Clave_Municipio', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Periodos',
            fields=[
                ('Clave_Periodo', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RVOES',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreCarrera', models.CharField(max_length=200)),
                ('TotalAlumnos', models.IntegerField()),
                ('TotalPrimero', models.IntegerField()),
                ('TotalSegundo', models.IntegerField()),
                ('TotalTercero', models.IntegerField()),
                ('TotalCuarto', models.IntegerField()),
                ('TotalQuinto', models.IntegerField()),
                ('TotalSexto', models.IntegerField()),
                ('TotalHombres', models.IntegerField()),
                ('TotalMujeres', models.IntegerField()),
                ('Tipo', models.CharField(max_length=50)),
                ('Area', models.CharField(max_length=100)),
                ('ClaveCarrera', models.CharField(max_length=30)),
                ('Modalidad', models.CharField(max_length=25)),
                ('Periodos', models.CharField(max_length=25)),
                ('modificando', models.BooleanField(default=False)),
                ('ClaveEscuela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SigApp.EscuelaC')),
            ],
        ),
        migrations.CreateModel(
            name='RVOE',
            fields=[
                ('IdRVOE', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Clave_Carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SigApp.Carrera')),
                ('Clave_GradoAcademico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SigApp.GradoAcademico')),
                ('Clave_Institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SigApp.Institucion')),
                ('Clave_Modalidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SigApp.Modalidad')),
                ('Clave_Periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SigApp.Periodos')),
            ],
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('Clave_Localidad', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=70)),
                ('Clave_Municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SigApp.Municipio')),
            ],
        ),
        migrations.CreateModel(
            name='estadisticosNuevo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TotalAlumnos', models.IntegerField()),
                ('TotalPrimero', models.IntegerField()),
                ('TotalSegundo', models.IntegerField()),
                ('TotalTercero', models.IntegerField()),
                ('TotalCuarto', models.IntegerField()),
                ('TotalQuinto', models.IntegerField()),
                ('TotalSexto', models.IntegerField()),
                ('TotalHombres', models.IntegerField()),
                ('TotalMujeres', models.IntegerField()),
                ('ClaveEscuela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SigApp.EscuelaC', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCarrera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=200)),
                ('Clave_Carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SigApp.Carrera')),
                ('Clave_Institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SigApp.Institucion')),
            ],
        ),
        migrations.CreateModel(
            name='DatosEstadisticos',
            fields=[
                ('FechaRegistro', models.DateTimeField(primary_key=True, serialize=False)),
                ('totalAlumnos', models.BigIntegerField()),
                ('totalAlumnosFemenino', models.BigIntegerField()),
                ('totalAlumnosMasculino', models.BigIntegerField()),
                ('totalAlumnosIndigenas', models.BigIntegerField()),
                ('alumnosIndigenasM', models.BigIntegerField()),
                ('alumnosIndigenasF', models.BigIntegerField()),
                ('alumnosPrimerGrado', models.IntegerField()),
                ('AlumnosIndigenasPrimerGrado', models.BigIntegerField()),
                ('alumnosPrimerGradoHombres', models.IntegerField()),
                ('alumnosPrimerGradoMujeres', models.IntegerField()),
                ('alumnosIPrimerGradoHombres', models.IntegerField()),
                ('alumnosIPrimerGradoMujeres', models.IntegerField()),
                ('alumnosSegundoGrado', models.IntegerField()),
                ('AlumnosIndigenasSegundoGrado', models.BigIntegerField()),
                ('alumnosSegundoGradoHombres', models.IntegerField()),
                ('alumnosSegundoGradoMujeres', models.IntegerField()),
                ('alumnosISegundoGradoHombres', models.IntegerField()),
                ('alumnosISegundoGradoMujeres', models.IntegerField()),
                ('alumnosTercerGrado', models.IntegerField()),
                ('AlumnosIndigenasTercerGrado', models.BigIntegerField()),
                ('alumnosTercerGradoHombres', models.IntegerField()),
                ('alumnosTercerGradoMujeres', models.IntegerField()),
                ('alumnosITercerGradoHombres', models.IntegerField()),
                ('alumnosITercerGradoMujeres', models.IntegerField()),
                ('alumnosCuartoGrado', models.IntegerField()),
                ('AlumnosIndigenasCuartoGrado', models.BigIntegerField()),
                ('alumnosCuartoGradoHombres', models.IntegerField()),
                ('alumnosCuartoGradoMujeres', models.IntegerField()),
                ('alumnosICuartoGradoHombres', models.IntegerField()),
                ('alumnosICuartoGradoMujeres', models.IntegerField()),
                ('alumnosQuintoGrado', models.IntegerField()),
                ('AlumnosIndigenasQuintoGrado', models.BigIntegerField()),
                ('alumnosQuintoGradoHombres', models.IntegerField()),
                ('alumnosQuintoGradoMujeres', models.IntegerField()),
                ('alumnosIQuintoGradoHombres', models.IntegerField()),
                ('alumnosIQuintoGradoMujeres', models.IntegerField()),
                ('alumnosSextoGrado', models.IntegerField()),
                ('AlumnosIndigenasSextoGrado', models.BigIntegerField()),
                ('alumnosSextoGradoHombres', models.IntegerField()),
                ('alumnosSextoGradoMujeres', models.IntegerField()),
                ('alumnosISextoGradoHombres', models.IntegerField()),
                ('alumnosISextoGradoMujeres', models.IntegerField()),
                ('IdRVOE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SigApp.RVOE')),
            ],
        ),
        migrations.CreateModel(
            name='UbicacionCentroTrabajo',
            fields=[
                ('Clave_CentroTrabajo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='SigApp.CentroTrabajo')),
                ('direccion', models.CharField(max_length=250)),
                ('Localidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SigApp.Localidad')),
            ],
        ),
    ]
