# Generated by Django 3.2.25 on 2024-10-22 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_pages', '0008_alter_extendedperson_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmbedCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('code', models.TextField(max_length=500, verbose_name='Тег iframe для встраиваемого содержимого')),
            ],
            options={
                'verbose_name': 'Встраиваемое содержимое',
                'verbose_name_plural': 'Встраиваемое содержимое',
            },
        ),
    ]
