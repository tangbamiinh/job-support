# Generated by Django 4.1 on 2022-08-04 07:13

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Job",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=30)),
                ("location", models.CharField(max_length=30)),
                ("published_date", models.DateTimeField(auto_now_add=True)),
                ("vacancy_count", models.IntegerField(default=0)),
                ("job_nature", models.CharField(max_length=30)),
                ("salary_start", models.IntegerField(default=0)),
                ("salary_end", models.IntegerField(default=0)),
                ("company_detail", tinymce.models.HTMLField()),
            ],
        ),
    ]
