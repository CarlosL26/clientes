# Generated by Django 4.2.4 on 2023-09-28 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rubro', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=40)),
                ('domicilio', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Clientes',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
    ]
