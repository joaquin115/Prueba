# Generated by Django 4.0.5 on 2022-07-14 04:54

import django.contrib.auth.base_user
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PruebaFinalApp', '0007_alter_publicaciones_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicaciones',
            name='usuario',
            field=models.CharField(default=django.contrib.auth.base_user.AbstractBaseUser.get_username, max_length=50),
        ),
    ]
