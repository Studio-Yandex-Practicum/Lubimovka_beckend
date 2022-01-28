# Generated by Django 3.2.11 on 2022-01-27 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20220123_1450'),
        ('library', '0022_auto_20220126_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='core.person', verbose_name='Человек'),
        ),
    ]
