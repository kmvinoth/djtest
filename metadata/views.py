from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.core.exceptions import FieldError, ObjectDoesNotExist
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import ProjectMetadataForm
from .models import ProjectMetadata
from projects.models import Project


@user_passes_test(lambda u: u.groups.filter(name='Project Admin').exists(), login_url='/projects/user_dashboard')
@login_required(login_url='/accounts/login')
def project_metadata(request, prj_name):
    try:
        prj = Project.objects.get(project_name=prj_name)
        get_project = ProjectMetadata.objects.get(project=prj.id)
        return admin_projects_edit_project_metadata(request, prj_name)
    except ProjectMetadata.DoesNotExist:
        return render(request, 'metadata/project_metadata.html', {'project_name': prj_name})


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


@user_passes_test(lambda u: u.groups.filter(name='Project Admin').exists(), login_url='/projects/user_dashboard')
@login_required(login_url='/accounts/login')
def admin_projects_edit_project_metadata(request, prj_name):
    prj = Project.objects.get(project_name=prj_name)
    get_project = get_object_or_404(ProjectMetadata, project=prj.id)
    if request.method == 'POST':
        project_edit_metadata_form = ProjectMetadataForm(request.POST, instance=get_project)
        if project_edit_metadata_form.is_valid():
            project_edit_metadata_form.save()
            return redirect('/projects/admin')
        else:
            error = True
            # project_edit_form.fields['admin'] = forms.ModelChoiceField(User.objects.filter(username=request.user))
            return render(request, 'metadata/edit_project_metadata.html',
                          {'project_edit_metadata_form': project_edit_metadata_form, 'error': error, 'project_name': prj_name})
    else:
        project_edit_form = ProjectMetadataForm(initial={'project_name': prj_name, 'admin': request.user},
                                                instance=get_project)
        # project_edit_form.fields['admin'] = forms.ModelChoiceField(User.objects.filter(username=request.user))
        return render(request, 'metadata/edit_project_metadata.html',
                      {'project_edit_form': project_edit_form, 'project_name': prj_name})


@login_required(login_url='/accounts/login')
def member_metadata_view(request, prj_name):
    prj = Project.objects.get(project_name=prj_name)
    return render(request, 'metadata/member_metadata_dashboard.html', {'project_name': prj})

