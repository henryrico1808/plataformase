# Generated by Django 2.2.1 on 2020-05-13 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20200512_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarioinstitucion',
            name='cct',
            field=models.TextField(blank=True, null=True, unique=True),
        ),
    ]
