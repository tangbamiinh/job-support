from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('category', views.category, name='category'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('notfound', views.notfound, name='notfound'),
    path('jobs/<int:job_id>', views.job_detail, name='job_detail'),
    path('jobs/', views.job_list, name='job_list'),
    path('tinymce/', include('tinymce.urls')),
]
