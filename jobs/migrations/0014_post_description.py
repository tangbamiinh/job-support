# Generated by Django 4.1 on 2022-08-07 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0013_post_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="description",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
    ]
