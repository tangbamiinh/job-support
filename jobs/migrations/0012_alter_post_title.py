# Generated by Django 4.1 on 2022-08-07 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0011_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post", name="title", field=models.CharField(max_length=100),
        ),
    ]
