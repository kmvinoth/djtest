from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.core.exceptions import FieldError, ObjectDoesNotExist
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import MetadataForm, value_inline_form_set
from .models import Value, MetadataAttributes
from projects.models import Project


# @user_passes_test(lambda u: u.groups.filter(name='Project Admin').exists(), login_url='/projects/user_dashboard')
# @login_required(login_url='/accounts/login')
# def project_metadata(request, prj_name):
#     try:
#         prj = Project.objects.get(project_name=prj_name)
#         get_project = ProjectMetadata.objects.get(project=prj.id)
#         return admin_projects_edit_project_metadata(request, prj_name)
#     except ProjectMetadata.DoesNotExist:
#         return render(request, 'metadata/project_metadata.html', {'project_name': prj_name})


@user_passes_test(lambda u: u.groups.filter(name='Project Admin').exists(), login_url='/projects/user_dashboard')
@login_required(login_url='/accounts/login')
def add_project_metadata(request, prj_name):
    prj_inst = Project.objects.get(project_name=prj_name)
    if request.method == 'POST':
        value_formset = value_inline_form_set(request.POST, request.FILES, instance=prj_inst)
        if value_formset.is_valid():
            value_formset.save()
            return redirect('/projects/admin')
        else:
            error = True
            print(error)
            value_formset = value_inline_form_set(instance=prj_inst)
            return render(request, 'metadata/add_project_metadata.html', {'formset': value_formset, 'error': error,
                                                                          'project_name': prj_name})
    else:
        value_formset = value_inline_form_set(instance=prj_inst)
        return render(request, 'metadata/add_project_metadata.html', {'formset': value_formset,
                                                                      'project_name': prj_name})


@login_required(login_url='/accounts/login')
def member_metadata_view(request, prj_name):
    prj = Project.objects.get(project_name=prj_name)
    return render(request, 'metadata/member_metadata_dashboard.html', {'project_name': prj})

