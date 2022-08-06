from django.db import models
from django.db.models import F
from django.db.models.signals import post_save
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _


class JobCategory(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='images/', null=True, blank=True)

    number_of_jobs = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "job categories"

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    class JobNatures(models.TextChoices):
        FULL_TIME = 'FULL_TIME', _('Full Time')
        PART_TIME = 'PART_TIME', _('Part Time')
        CONTRACT = 'CONTRACT', _('Contract')
        INTERNSHIP = 'INTERNSHIP', _('Internship')
        OTHER = 'OTHER', _('Other')

    title = models.CharField(max_length=30)
    description = HTMLField(default="")
    published_date = models.DateTimeField(auto_now_add=True)
    vacancy_count = models.PositiveIntegerField(default=0)
    job_nature = models.CharField(max_length=30, choices=JobNatures.choices, default=JobNatures.FULL_TIME)
    salary_start = models.PositiveIntegerField(default=0)
    salary_end = models.PositiveIntegerField(default=0)
    company_detail = HTMLField()
    logo = models.ImageField(upload_to='images/', null=True, blank=True)

    categories = models.ManyToManyField(JobCategory, related_name='jobs')
    locations = models.ManyToManyField(Location, related_name='jobs')


def on_job_created(sender, instance, created, **kwargs):
    if created:
        job = instance
        for category in job.categories:
            category.number_of_jobs += F('number_of_jobs') + 1
            category.save(update_fields=['number_of_jobs'])


post_save.connect(on_job_created, sender=Job)
