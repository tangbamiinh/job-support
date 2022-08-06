from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, TemplateView

from jobs.models import Job, JobCategory, Location


def index(request):
    jobs = Job.objects.all()
    job_categories = JobCategory.objects.all()
    locations = Location.objects.all()

    return render(request, 'index.html', {
        'featured_job_list': jobs,
        # 'full_time_job_list': jobs.filter(job_nature='FULL_TIME'),
        # 'part_time_job_list': jobs.filter(job_nature='PART_TIME'),
        'job_categories': job_categories,
        'locations': locations,
    })


def about(request):
    return render(request, 'about.html', {'title': 'About'})


def contact(request):
    return render(request, 'contact.html', {'title': 'Contact'})


def job_detail(request, job_id: int):
    job = Job.objects.get(id=job_id)
    return render(request, 'job-detail.html', {'title': 'Job Detail', 'job': job})


def job_list(request, keyword: str = None):
    if keyword:
        jobs = Job.objects.filter(title__icontains=keyword)
    else:
        jobs = Job.objects.all()
    return render(request, 'job-list.html', {'title': 'Job List', 'job_list': jobs})


class JobSearchResultsView(ListView):
    model = Job
    template_name = 'job-list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        location_id = self.request.GET.get('location')
        category_id = self.request.GET.get('category')

        if query:
            queryset = Job.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )
        else:
            queryset = Job.objects.all()

        if location_id:
            queryset = queryset.filter(locations__id=location_id)
        if category_id and category_id != '0':
            queryset = queryset.filter(categories__id=category_id)

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Job Search Results'

        print(context)
        return context


def category_list(request):
    job_categories = JobCategory.objects.all()
    return render(request, 'category-list.html', {'title': 'Category', 'job_categories': job_categories})


def category_detail(request, category_id: int):
    job_category = JobCategory.objects.get(id=category_id)
    print(job_category)
    jobs = job_category.jobs.all()
    print(len(jobs))
    return render(request, 'category-detail.html',
                  {'title': f'Category: {job_category.name}', 'job_category': job_category, 'job_list': jobs})


def testimonial(request):
    return render(request, 'testimonial.html', {'title': 'Testimonial'})


def notfound(request):
    return render(request, '404.html', {'title': '404'})
