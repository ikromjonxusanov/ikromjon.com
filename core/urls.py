from django.urls import path

from core.views import home, about, projects, project, blogs, blog

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('projects', projects, name='projects'),
    path('projects/<int:pk>', project, name='project-detail'),
    path('blogs', blogs, name='blogs'),
    path('blogs/<int:pk>', blog, name='blog-detail'),
]