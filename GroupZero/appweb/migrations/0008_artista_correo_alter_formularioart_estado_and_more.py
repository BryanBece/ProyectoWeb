# Generated by Django 4.2.2 on 2023-06-25 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0007_alter_artista_usuario_alter_obra_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='artista',
            name='correo',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='formularioart',
            name='estado',
            field=models.IntegerField(choices=[(0, 'En Espera de Aprobación'), (1, 'En Exhibición'), (2, 'Vendida')]),
        ),
        migrations.AlterField(
            model_name='obra',
            name='estado',
            field=models.IntegerField(choices=[(0, 'En Espera de Aprobación'), (1, 'En Exhibición'), (2, 'Vendida')], default=0),
        ),
    ]
