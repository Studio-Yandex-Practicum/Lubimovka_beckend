# Generated by Django 3.2.11 on 2022-01-29 14:40

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField(verbose_name='Дата начала фестиваля')),
                ('end_date', models.DateField(verbose_name='Дата окончания фестиваля')),
                ('description', models.CharField(max_length=200, verbose_name='Описание фестиваля')),
                ('year', models.PositiveSmallIntegerField(default=2022, unique=True, validators=[django.core.validators.MinValueValidator(1990), django.core.validators.MaxValueValidator(2500)], verbose_name='Год фестиваля')),
                ('plays_count', models.PositiveIntegerField(default=1, verbose_name='Общее количество пьес')),
                ('selected_plays_count', models.PositiveSmallIntegerField(default=1, verbose_name='Количество отобранных пьес')),
                ('selectors_count', models.PositiveSmallIntegerField(default=1, verbose_name='Количество отборщиков пьес')),
                ('volunteers_count', models.PositiveSmallIntegerField(default=1, verbose_name='Количество волонтёров фестиваля')),
                ('events_count', models.PositiveSmallIntegerField(default=1, verbose_name='Количество событий фестиваля')),
                ('cities_count', models.PositiveSmallIntegerField(default=1, verbose_name='Количество участвующих городов')),
                ('video_link', models.URLField(max_length=250, verbose_name='Ссылка на видео о фестивале')),
                ('blog_entries', models.CharField(max_length=10, verbose_name='Записи в блоге о фестивале')),
                ('press_release_image', models.ImageField(upload_to='', verbose_name='Изображение для страницы пресс-релизов')),
            ],
            options={
                'verbose_name': 'Фестиваль',
                'verbose_name_plural': 'Фестивали',
                'ordering': ['-year'],
            },
        ),
        migrations.CreateModel(
            name='FestivalTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('team', models.CharField(choices=[('art', 'Арт-дирекция фестиваля'), ('fest', 'Команда фестиваля')], max_length=5, verbose_name='Тип команды')),
                ('position', models.CharField(max_length=150, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Команда фестиваля',
                'verbose_name_plural': 'Команды фестиваля',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('type', models.CharField(choices=[('general', 'Генеральный партнер'), ('festival', 'Партнер фестиваля'), ('info', 'Информационный партнер')], max_length=8, verbose_name='Тип')),
                ('url', models.URLField(verbose_name='Ссылка на сайт')),
                ('image', models.ImageField(help_text='Загрузите логотип партнёра', upload_to='images/info/partnerslogo', verbose_name='Логотип')),
                ('in_footer_partner', models.BooleanField(default=False, help_text='Поставьте галочку, чтобы показать логотип партнёра внизу страницы', verbose_name='Отображать внизу страницы')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнеры',
                'ordering': ('type',),
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(max_length=255, verbose_name='Описание')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('address', models.CharField(max_length=50, verbose_name='Адрес')),
                ('map_link', models.URLField(verbose_name='Ссылка на карту')),
            ],
            options={
                'verbose_name': 'Площадка',
                'verbose_name_plural': 'Площадки',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('question', models.TextField(max_length=500, validators=[django.core.validators.MinLengthValidator(2, 'Вопрос должен состоять более чем из 2 символов')], verbose_name='Текст вопроса')),
                ('author_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('author_email', models.EmailField(max_length=50, verbose_name='Электронная почта')),
            ],
            options={
                'verbose_name': 'Вопрос или предложение',
                'verbose_name_plural': 'Вопросы или предложения',
            },
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('review_title', models.CharField(blank=True, max_length=50, verbose_name='Заголовок отзыва')),
                ('review_text', models.TextField(blank=True, max_length=500, verbose_name='Текст отзыва')),
                ('festival', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volunteers', to='info.festival', verbose_name='Фестиваль')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.person', verbose_name='Человек')),
            ],
            options={
                'verbose_name': 'Волонтёр фестиваля',
                'verbose_name_plural': 'Волонтёры фестиваля',
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('position', models.CharField(max_length=150, verbose_name='Должность')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='core.person', verbose_name='Человек')),
            ],
            options={
                'verbose_name': 'Попечитель фестиваля',
                'verbose_name_plural': 'Попечители фестиваля',
            },
        ),
        migrations.CreateModel(
            name='PressRelease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=500, unique=True, verbose_name='Заголовок')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Текст')),
                ('festival', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='press_releases', to='info.festival', verbose_name='Фестиваль')),
            ],
            options={
                'verbose_name': 'Пресс-релиз',
                'verbose_name_plural': 'Пресс-релизы',
                'ordering': ('-created',),
            },
        ),
        migrations.AddConstraint(
            model_name='place',
            constraint=models.UniqueConstraint(fields=('name', 'city'), name='unique_place'),
        ),
        migrations.AddField(
            model_name='festivalteam',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.person', verbose_name='Человек'),
        ),
        migrations.AddField(
            model_name='festival',
            name='images',
            field=models.ManyToManyField(related_name='festivalimages', to='core.Image', verbose_name='Изображения'),
        ),
        migrations.AddConstraint(
            model_name='volunteer',
            constraint=models.UniqueConstraint(fields=('person', 'festival'), name='unique_volunteer'),
        ),
        migrations.AddConstraint(
            model_name='festivalteam',
            constraint=models.UniqueConstraint(fields=('person', 'team'), name='unique_person_team'),
        ),
        migrations.AddConstraint(
            model_name='festival',
            constraint=models.CheckConstraint(check=models.Q(('start_date__lt', django.db.models.expressions.F('end_date'))), name='start_date_before_end_date'),
        ),
    ]
