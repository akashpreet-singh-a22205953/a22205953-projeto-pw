# Generated by Django 4.0.6 on 2024-05-30 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio1', '0004_techpresentation'),
    ]

    operations = [
        migrations.CreateModel(
            name='allApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bnadas', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('Lei', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('Artigos', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('Meteo', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
