from django.contrib import admin

# Register your models here.
from jobs.models import Job, JobCategory, Location, Post


class JobCategoryAdmin(admin.ModelAdmin):
    save_as = True
    search_fields = ['name']
    search_help_text = 'Search by job category name'
    sortable_by = ['name']
    view_on_site = True

    list_display = ('name', 'id', 'description')


class LocationAdmin(admin.ModelAdmin):
    save_as = True
    search_fields = ['name']
    search_help_text = 'Search by location name'
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
        'title', 'id', 'published_date', 'vacancy_count', 'job_nature', 'salary_start', 'salary_end')


class PostAdmin(admin.ModelAdmin):
    save_as = True
    search_fields = ['title']
    search_help_text = 'Search by post title'
    sortable_by = ['title']
    view_on_site = True

    list_display = ('title', 'id', 'published_date')


admin.site.register(Job, JobAdmin)
admin.site.register(JobCategory, JobCategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
