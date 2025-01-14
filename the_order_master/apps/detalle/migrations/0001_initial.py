# Generated by Django 5.1 on 2024-10-18 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetallePedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modo_entrega', models.CharField(choices=[('llevar', 'Para llevar'), ('aqui', 'Para consumir en el sitio')], max_length=50)),
                ('cantidad', models.PositiveIntegerField()),
                ('observaciones', models.TextField(blank=True)),
            ],
        ),
    ]
