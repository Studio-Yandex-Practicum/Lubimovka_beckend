# Generated by Django 3.2.12 on 2022-05-05 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0015_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('plays_links', 'Пьесы'), ('additional_links', 'Дополнительно')], max_length=25, verbose_name='Тип ссылки')),
                ('title', models.CharField(max_length=100, verbose_name='Название ссылки')),
                ('link', models.URLField()),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Порядковый номер ссылки')),
                ('festival', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='infolinks', to='info.festival', verbose_name='Прочие ссылки')),
            ],
            options={
                'verbose_name': 'Ссылка с описанием',
                'verbose_name_plural': 'Ссылки с описанием',
                'ordering': ('order',),
            },
        ),
    ]
