from django.conf.urls.static import static
from django.urls import path, include

from mySite import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('categories', views.category_list, name='categories'),
    path('categories/<int:category_id>', views.category_detail, name='category_detail'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('notfound', views.notfound, name='notfound'),
    path('jobs/<int:job_id>', views.job_detail, name='job_detail'),
    path('jobs/', views.JobSearchResultsView.as_view(), name='job_list'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:post_id>', views.post_detail, name='post_detail'),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
