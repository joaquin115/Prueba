# Generated by Django 4.0.5 on 2022-07-14 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PruebaFinalApp', '0008_publicaciones_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicaciones',
            name='usuario',
            field=models.CharField(max_length=50),
        ),
    ]
