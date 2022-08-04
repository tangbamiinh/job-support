from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from jobs.models import Job


def index(request):
    return render(request, 'index.html', {'jobs': Job.objects.all()})


def about(request):
    return render(request, 'about.html', {'title': 'About'})


def contact(request):
    return render(request, 'contact.html', {'title': 'Contact'})


def job_detail(request, job_id: int):
    return render(request, 'job-detail.html', {'title': 'Job Detail', 'job': Job.objects.get(id=job_id)})


def job_list(request, keyword: str):
    jobs = Job.objects.filter(title__contains=keyword)
    return render(request, 'job-list.html', {'title': 'Job List', 'jobs': jobs})


def category(request):
    return render(request, 'category.html', {'title': 'Category'})


def testimonial(request):
    return render(request, 'testimonial.html', {'title': 'Testimonial'})


def notfound(request):
    return render(request, '404.html', {'title': '404'})
