# Generated by Django 4.0.5 on 2022-07-17 01:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PruebaFinalApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
                ('pais', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('fecha_viaje', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Publicaciones',
                'db_table': 'imageupload',
            },
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='media')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
