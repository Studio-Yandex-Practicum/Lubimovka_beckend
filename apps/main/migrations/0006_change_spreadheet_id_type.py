# Generated by Django 3.2.25 on 2024-05-22 21:01
import re

from django.db import migrations


def switch_type_to_url(apps, schema_editor):
    Setting = apps.get_model("core", "Setting")
    spreadsheet_id = Setting.objects.get(settings_key="SPREADSHEET_ID").text
    spreadsheet_url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/edit" if spreadsheet_id else ""
    Setting.objects.filter(settings_key="SPREADSHEET_ID").update(field_type="URL", description="Ссылка на Google-таблицу", url=spreadsheet_url, text="")


def switch_type_to_text(apps, schema_editor):
    Setting = apps.get_model("core", "Setting")
    spreadsheet_url = Setting.objects.get(settings_key="SPREADSHEET_ID").url
    spreadsheet_id = re.search(r"\/spreadsheets\/d\/(?P<id>.+)\/", spreadsheet_url).group("id") if spreadsheet_url else ""
    Setting.objects.filter(settings_key="SPREADSHEET_ID").update(field_type="TEXT", description="id Google таблицы", url="", text=spreadsheet_id)


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_banner_options'),
    ]

    operations = [
        migrations.RunPython(code=switch_type_to_url, reverse_code=switch_type_to_text)
    ]
