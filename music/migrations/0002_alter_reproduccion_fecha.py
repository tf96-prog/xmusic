# Generated by Django 5.1.4 on 2025-01-16 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reproduccion',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]
