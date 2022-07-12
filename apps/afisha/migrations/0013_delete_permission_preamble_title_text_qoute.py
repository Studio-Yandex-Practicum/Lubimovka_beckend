# Generated by Django 3.2.13 on 2022-07-12 16:12
from django.core.exceptions import ObjectDoesNotExist
from django.db import migrations


def delete_preamble_permission(apps, schema_editor):
    """Remove not supported content from projects."""
    PermissionType = apps.get_model("auth", "Permission")

    try:
        preamble_permission = PermissionType.objects.filter(content_type__model="preamble")
    except ObjectDoesNotExist:
        return
    preamble_permission.delete()


def delete_quote_permission(apps, schema_editor):
    """Remove not supported content from projects."""
    PermissionType = apps.get_model("auth", "Permission")

    try:
        quote_permission = PermissionType.objects.filter(content_type__model="quote")
    except ObjectDoesNotExist:
        return
    quote_permission.delete()


def delete_text_permission(apps, schema_editor):
    """Remove not supported content from projects."""
    PermissionType = apps.get_model("auth", "Permission")

    try:
        text_permission = PermissionType.objects.filter(content_type__model="text")
    except ObjectDoesNotExist:
        return
    text_permission.delete()


def delete_title_permission(apps, schema_editor):
    """Remove not supported content from projects."""
    PermissionType = apps.get_model("auth", "Permission")

    try:
        title_permission = PermissionType.objects.filter(content_type__model="title")
    except ObjectDoesNotExist:
        return
    title_permission.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0012_alter_performance_duration'),
    ]

    operations = [
        migrations.RunPython(
            delete_preamble_permission,
        ),
        migrations.RunPython(
            delete_quote_permission,
        ),
        migrations.RunPython(
            delete_text_permission,
        ),
        migrations.RunPython(
            delete_title_permission,
        ),
    ]
