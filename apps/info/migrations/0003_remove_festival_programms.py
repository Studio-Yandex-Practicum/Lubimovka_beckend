# Generated by Django 3.2.7 on 2021-10-02 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="festival",
            name="programms",
        ),
    ]
