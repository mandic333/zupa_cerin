# Generated by Django 3.2 on 2021-04-21 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_glasnici_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glasnici',
            name='slika',
            field=models.ImageField(upload_to=''),
        ),
    ]
