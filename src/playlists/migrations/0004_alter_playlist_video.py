# Generated by Django 3.2.19 on 2023-05-30 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
        ('playlists', '0003_auto_20230530_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='playlist_featured', to='videos.video'),
        ),
    ]
