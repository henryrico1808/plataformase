# Generated by Django 2.2.1 on 2020-08-12 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SETyRS', '0002_notificaciones_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitudexamen',
            name='hora_exa',
            field=models.CharField(default='12:00', max_length=10),
        ),
    ]
