# Generated by Django 4.0.6 on 2024-05-02 19:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('isbn', models.CharField(max_length=15)),
                ('author', models.CharField(max_length=25)),
                ('pub_Date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
