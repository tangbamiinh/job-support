from django.db import models
from tinymce.models import HTMLField


class JobCategory(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)


class Job(models.Model):
    class JobNatures(models.TextChoices):
        FULL_TIME = 'FULL_TIME'
        PART_TIME = 'PART_TIME'
        CONTRACT = 'CONTRACT'
        INTERNSHIP = 'INTERNSHIP'
        OTHER = 'OTHER'

    title = models.CharField(max_length=30)
    description = HTMLField(default="")
    location = models.CharField(max_length=30)
    published_date = models.DateTimeField(auto_now_add=True)
    vacancy_count = models.IntegerField(default=0)
    job_nature = models.CharField(max_length=30, choices=JobNatures.choices, default=JobNatures.FULL_TIME)
    salary_start = models.IntegerField(default=0)
    salary_end = models.IntegerField(default=0)
    company_detail = HTMLField()

    categories = models.ManyToManyField(JobCategory, related_name='jobs')
