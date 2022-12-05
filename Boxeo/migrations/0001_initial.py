# Generated by Django 4.1.3 on 2022-12-04 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boxeador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('peso', models.FloatField()),
                ('cinturones', models.IntegerField()),
                ('ko', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('nacionalidad', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=20)),
                ('titulos', models.IntegerField()),
                ('entrenador', models.CharField(max_length=60)),
                ('lesionados', models.CharField(max_length=15)),
                ('boxeador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Boxeo.boxeador')),
            ],
        ),
        migrations.CreateModel(
            name='Torneo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('ubicacion', models.CharField(max_length=50)),
                ('cupos', models.IntegerField()),
                ('categoria', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
                ('inscripcion', models.CharField(max_length=20)),
                ('inscritos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Boxeo.team')),
            ],
        ),
    ]
