from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.core.exceptions import FieldError, ObjectDoesNotExist
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import ProjectMetadataForm


@user_passes_test(lambda u: u.groups.filter(name='Project Admin').exists(), login_url='/projects/user_dashboard')
@login_required(login_url='/accounts/login')
def add_project_metadata(request, prj_name):
    if request.method == 'POST':
        project_metadata_form = ProjectMetadataForm(request.POST)
        if project_metadata_form.is_valid():
            project_metadata_form.save()
            return redirect('/projects/admin')
        else:
            error = True
            return render(request, 'metadata/add_project_metadata.html',
                          {'project_metadata_form': project_metadata_form, 'error': error, 'project_name': prj_name})
    else:
        project_metadata_form = ProjectMetadataForm()
        return render(request, 'metadata/add_project_metadata.html',
                      {'project_metadata_form': project_metadata_form, 'project_name': prj_name})
