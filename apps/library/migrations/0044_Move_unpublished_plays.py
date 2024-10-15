# Generated by Django 3.2.25 on 2024-10-09 14:29

from pathlib import Path

from django.conf import settings
from django.db import migrations

from apps.library.services import hide_play_file, restore_play_file


def hide_plays(apps, schema_editor):
    Play = apps.get_model("library", "play")
    plays = Play.objects.filter(published=False)
    for play in plays:
        hide_play_file(play)


def restore_plays(apps, schema_editor):
    Play = apps.get_model("library", "play")
    plays = Play.objects.filter(published=False)
    for play in plays:
        restore_play_file(play)


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0043_alter_socialnetworklink_name'),
    ]

    operations = [
        migrations.RunPython(hide_plays, restore_plays)
    ]
