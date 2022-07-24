# Generated by Django 3.2.13 on 2022-07-24 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0017_merge_20220724_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterclass',
            name='supplemental_text',
            field=models.TextField(blank=True, help_text='Описание, расположенное под изображением', max_length=500, verbose_name='Дополнительное описание'),
        ),
        migrations.AddField(
            model_name='reading',
            name='supplemental_text',
            field=models.TextField(blank=True, help_text='Описание, расположенное под изображением', max_length=500, verbose_name='Дополнительное описание'),
        ),
    ]
