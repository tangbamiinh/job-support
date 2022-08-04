from django.contrib import admin

# Register your models here.
from jobs.models import Job, JobCategory


class JobCategoryAdmin(admin.ModelAdmin):
    save_as = True
    search_fields = ['name']
    search_help_text = 'Search by job category name'
    sortable_by = ['name']
    view_on_site = True

    list_display = ('name', 'id', 'description')


class JobAdmin(admin.ModelAdmin):
    save_as = True
    search_fields = ['title']
    search_help_text = 'Search by job title'
    sortable_by = ['title']
    view_on_site = True

    list_display = (
        'title', 'id', 'location', 'published_date', 'vacancy_count', 'job_nature', 'salary_start', 'salary_end')


admin.site.register(Job, JobAdmin)
admin.site.register(JobCategory, JobCategoryAdmin)
