# Generated by Django 4.1 on 2022-08-04 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0005_jobcategory_remove_job_job_category_job_categories"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobcategory",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
