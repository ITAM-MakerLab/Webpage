from django.shortcuts import render, get_object_or_404
from .models import Project


# Create your views here.
def projectIndex(request):
    recent_projects = Project.objects.order_by("uploadDateTime").reverse()
    projectsIndex_context = {"recent_projects": recent_projects}
    return render(request, "proyectos/projectsIndex.html", projectsIndex_context)


def projectDetail(request, project_id):
    selected_project = get_object_or_404(Project, pk=project_id)
    project_context = {"project": selected_project}
    return render(request, "proyectos/projectDetail.html", project_context)
