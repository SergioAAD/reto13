# Generated by Django 3.2.5 on 2021-07-07 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_alter_ingreso_notas_nota'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingreso_asistencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('class_date', models.DateField()),
                ('content', models.TextField()),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.alumno')),
                ('asistencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.asistencia')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cursos')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.periodos')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ingreso Asistencia',
                'verbose_name_plural': 'Ingreso Asistencias',
                'db_table': 'ingresoasistencia',
                'ordering': ['id'],
            },
        ),
    ]
