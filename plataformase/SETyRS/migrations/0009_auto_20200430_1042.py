# Generated by Django 2.2.1 on 2020-04-30 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SETyRS', '0008_auto_20200426_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='sinodales',
            name='institucion',
            field=models.CharField(default='Instituto Tecnologico de Tepic', max_length=50),
        ),
        migrations.AlterField(
            model_name='notificacionadmin',
            name='departamento_id',
            field=models.IntegerField(default=1),
        ),
    ]