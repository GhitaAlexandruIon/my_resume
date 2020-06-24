from django.shortcuts import render, get_object_or_404
from.models import Project, Skill


def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects, 'skills': skills})


def projects_detail(request, pk):
    projects = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/projects_detail.html', {'projects': projects})
