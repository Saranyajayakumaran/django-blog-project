# Generated by Django 3.2.25 on 2024-05-17 10:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_auto_20240517_1041'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='comments',
        ),
    ]
