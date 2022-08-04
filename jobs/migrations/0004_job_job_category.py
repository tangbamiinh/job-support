# Generated by Django 4.1 on 2022-08-04 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0003_alter_job_job_nature"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="job_category",
            field=models.CharField(
                choices=[
                    ("WEB", "Web"),
                    ("MOBILE", "Mobile"),
                    ("DATA_SCIENCE", "Data Science"),
                    ("ARCHITECTURE", "Architecture"),
                    ("OTHER", "Other"),
                ],
                default="WEB",
                max_length=30,
            ),
        ),
    ]