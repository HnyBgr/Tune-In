# Generated by Django 3.0.6 on 2020-07-16 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200715_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicinfo',
            name='day',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='musicinfo',
            name='month',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='musicinfo',
            name='year',
            field=models.IntegerField(),
        ),
    ]
