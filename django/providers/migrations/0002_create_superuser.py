# Generated by Django 2.1.7 on 2019-02-14 22:07
import os

from django.db import migrations
from django.contrib.auth import get_user_model


class Migration(migrations.Migration):

    dependencies = [
            ('providers', '0001_initial'),
    ]

    def generate_superuser(apps, schema_editor):
        """
        Create a superuser based on environment vars.
        """
        User = get_user_model()

        credentials = {}
        credentials['username'] = os.environ.get('DJANGO_SUPERUSER_NAME')
        credentials['email'] = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        credentials['password']= os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        superuser = User.objects.create_superuser(**credentials)
        superuser.save()

    operations = [
        migrations.RunPython(generate_superuser),
    ]
