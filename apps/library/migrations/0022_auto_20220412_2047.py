# Generated by Django 3.2.12 on 2022-04-12 17:47

from django.db import migrations, models
import django.db.models.deletion


def set_type_to_other_plays(apps, schema_editor):
    Plays = apps.get_model("library", "Play")
    Plays.objects.filter(program__slug="other_plays").update(other_play=True, program=None)

def delete_program(apps, shema_editor):
    ProgramType = apps.get_model("library", "ProgramType")
    ProgramType.objects.filter(slug="other_plays").delete()

class Migration(migrations.Migration):

    dependencies = [
        ('library', '0021_alter_play_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='play',
            name='other_play',
            field=models.BooleanField(default=False, help_text='Да/нет', verbose_name='Сторонняя пьеса'),
        ),
        migrations.AlterField(
            model_name='play',
            name='program',
            field=models.ForeignKey(blank=True, help_text='Для пьес Любимовки должна быть выбрана Программа', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='plays', to='library.programtype', verbose_name='Программа'),
        ),
        migrations.RunPython(
            set_type_to_other_plays,
        ),
        migrations.RunPython(
            delete_program,
        ),
    ]
