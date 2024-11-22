from django.urls import path

from core.views import home, about, projects, project

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('projects', projects, name='projects'),
    path('projects/<int:pk>', project, name='project-detail'),
]