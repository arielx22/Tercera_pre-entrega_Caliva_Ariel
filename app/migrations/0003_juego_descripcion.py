# Generated by Django 4.2 on 2023-06-04 17:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_juego_desarrollo_alter_juego_dispositivo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='juego',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
