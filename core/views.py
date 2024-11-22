from django.shortcuts import render, get_object_or_404

from core.models import Project


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def projects(request):
    ctx = {
        'projects': Project.objects.all()
    }
    return render(request, 'projects/list.html', context=ctx)

def project(request, pk):
    ctx = {
        'obj': get_object_or_404(Project, pk=pk)
    }
    return render(request, 'projects/detail.html', context=ctx)