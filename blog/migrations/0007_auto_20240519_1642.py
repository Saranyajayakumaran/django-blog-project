# Generated by Django 3.2.25 on 2024-05-19 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_comments_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_on']},
        ),
        migrations.AddField(
            model_name='post',
            name='challenge',
            field=models.FloatField(default=3.0),
        ),
        migrations.AddField(
            model_name='post',
            name='field_2',
            field=models.IntegerField(default=42),
        ),
        migrations.AddField(
            model_name='post',
            name='field_3',
            field=models.CharField(max_length=20, null=True),
        ),
    ]