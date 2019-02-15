# Generated by Django 2.1.7 on 2019-02-15 06:20

from django.db import migrations

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from ..models import Area


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0002_create_superuser'),
    ]

    def create_group(apps, schema_editor):
        """
        Create a group Providers with the basic permission to manipulate Area
        content type.
        """
        group, created = Group.objects.get_or_create(name='Providers')
        content_type = ContentType.objects.get_for_model(Area)
        permission_list = Permission.objects.filter(content_type=content_type)
        for permission in permission_list:
            group.permissions.add(permission)

    operations = [
        migrations.RunPython(create_group),
    ]