from django.urls import path

from core.views import home, about, mailru

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('mailru-domainSDLqlPJ857jj3Q5R.html', mailru, name='mailru'),
    # path('projects', projects, name='projects'),
    # path('projects/<int:pk>', project, name='project-detail'),
    # path('blogs', blogs, name='blogs'),
    # path('blogs/<int:pk>', blog, name='blog-detail'),
]
