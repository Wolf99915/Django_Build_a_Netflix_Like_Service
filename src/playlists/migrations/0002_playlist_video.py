# Generated by Django 3.2.19 on 2023-05-28 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
        ('playlists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='videos.video'),
        ),
    ]
