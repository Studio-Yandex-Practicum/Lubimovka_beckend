# Generated by Django 3.2.11 on 2022-01-23 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20220118_2233'),
        ('info', '0014_alter_volunteer_review_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='festivalteam',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.person', verbose_name='Человек'),
        ),
    ]
