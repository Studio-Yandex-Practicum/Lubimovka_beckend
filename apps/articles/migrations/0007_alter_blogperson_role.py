# Generated by Django 3.2.9 on 2021-12-04 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_0015_data_add_type_roles'),
        ('articles', '0006_auto_20211202_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogperson',
            name='role',
            field=models.ForeignKey(limit_choices_to={'type_roles__role_type': 'blog_persons_role'}, on_delete=django.db.models.deletion.RESTRICT, related_name='blog_persons', to='core.role', verbose_name='Роль в соавторстве'),
        ),
    ]
