# Generated by Django 2.2.1 on 2020-05-13 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SETyRS', '0015_auto_20200512_1756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitudexamen',
            old_name='presidente_id',
            new_name='id_presidente',
        ),
        migrations.RenameField(
            model_name='solicitudexamen',
            old_name='secretario_id',
            new_name='id_secretario',
        ),
        migrations.RenameField(
            model_name='solicitudexamen',
            old_name='vocal_id',
            new_name='id_vocal',
        ),
    ]
