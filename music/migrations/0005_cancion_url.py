# Generated by Django 5.1.4 on 2025-02-20 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_alter_album_options_alter_artista_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancion',
            name='url',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
    ]
