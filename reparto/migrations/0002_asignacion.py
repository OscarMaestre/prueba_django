# Generated by Django 2.1.1 on 2018-09-01 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reparto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reparto.Modulo')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reparto.Profesor')),
            ],
        ),
    ]
