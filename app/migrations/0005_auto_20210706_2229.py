# Generated by Django 3.2.5 on 2021-07-07 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_ingreso_notas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingreso_notas',
            name='nota',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Notas',
        ),
    ]
