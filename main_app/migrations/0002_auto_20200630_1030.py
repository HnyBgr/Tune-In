# Generated by Django 3.0.6 on 2020-06-30 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicinfo',
            name='date',
            field=models.DateField(verbose_name='dd-mm'),
        ),
    ]