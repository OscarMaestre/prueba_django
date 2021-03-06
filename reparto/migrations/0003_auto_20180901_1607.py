# Generated by Django 2.1.1 on 2018-09-01 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reparto', '0002_asignacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reparto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
            ],
        ),
        migrations.AddField(
            model_name='asignacion',
            name='reparto',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='reparto.Reparto'),
            preserve_default=False,
        ),
    ]
