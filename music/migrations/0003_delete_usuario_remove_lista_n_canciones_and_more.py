# Generated by Django 5.1.4 on 2025-01-16 16:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_alter_reproduccion_fecha'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.RemoveField(
            model_name='lista',
            name='n_canciones',
        ),
        migrations.RemoveField(
            model_name='reproduccion',
            name='id_cancion',
        ),
        migrations.AddField(
            model_name='album',
            name='artista',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='music.artista'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cancion',
            name='album',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='music.album'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cancion',
            name='colaboradores',
            field=models.ManyToManyField(to='music.artista'),
        ),
        migrations.AddField(
            model_name='cancion',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lista',
            name='canciones',
            field=models.ManyToManyField(to='music.cancion'),
        ),
        migrations.AddField(
            model_name='lista',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reproduccion',
            name='cancion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='music.cancion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='artista',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='cancion',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='lista',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='reproduccion',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
