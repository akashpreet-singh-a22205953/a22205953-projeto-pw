# Generated by Django 4.0.6 on 2024-04-24 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festivais', '0002_remove_localizacao_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='festival',
            name='bandas',
            field=models.ManyToManyField(blank=True, to='festivais.banda'),
        ),
    ]