from django.shortcuts import render, get_object_or_404
from.models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})


def projects_detail(request, pk):
    projects = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/projects_detail.html', {'projects': projects})
