# Generated by Django 2.2.1 on 2019-07-07 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SigApp', '0002_remove_detallecarrera_areainteres'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallecarrera',
            name='areaInteres',
            field=models.ForeignKey(default=21, on_delete=django.db.models.deletion.CASCADE, to='SigApp.AreaInteres'),
            preserve_default=False,
        ),
    ]
