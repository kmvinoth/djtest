"""
This module contains all the View functions related to the project
"""
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.core.exceptions import FieldError, ObjectDoesNotExist
from django.contrib.auth.decorators import user_passes_test, login_required
from django import forms
from .models import Project, User, ProjectMemberRole
from .forms import ProjectInfoForm, ProjectMemberRoleForm


@login_required(login_url='/accounts/login')
def project_member_view(request):
    """
    Return projects page (project Dashboard) to the user after successful login.

    If the user is in group Project Admin (created by portal(superuser) administrator),
    the user get's the Admin (project admin) link in his page,
    so that he can do admin activities for the specified project
    else the user gets the normal project member view.
    """

    member_inst = request.user.groups.filter(name='Project Admin').exists()
    if member_inst:
        admin_prjs = Project.objects.filter(admin=request.user)
        member_prjs = ProjectMemberRole.objects.filter(member=request.user)
        return render(request, 'projects/project_admin.html', {'member_projects': member_prjs,
                                                               'admin_projects': admin_prjs})
    else:
        member_prjs = ProjectMemberRole.objects.filter(member=request.user)  # returns Queryset
        return render(request, 'projects/project_member.html', {'member_projects': member_prjs})


# Better to use @permission required decorator to avoid code repetition, with a message permission denied
# @permission required decorator cannot be used as such for the default django User model.
#  see ref: https://docs.djangoproject.com/en/1.8/topics/auth/default/#topic-authorization
# @user_passes_test decorator is slow as well because you are hitting the database


@user_passes_test(lambda u: u.groups.filter(name='Project Admin').exists(), login_url='/projects/user_dashboard')
@login_required(login_url='/accounts/login')
def admin_projects_view(request):
    """
    Return admin projects page to the user, who has the role "Project Admin" and can perform project
    administration activities on individual project.
    """
    try:
        admin_prjs = Project.objects.filter(admin=request.user)
        return render(request, 'projects/admin_projects.html', {'admin_projects': admin_prjs})
    except FieldError:
        return HttpResponse('Some kind of problem with a model field')


@user_passes_test(lambda u: u.groups.filter(name='Project Admin').exists(), login_url='/projects/user_dashboard')
@login_required(login_url='/accounts/login')
def user_mgmt(request):
    """
    Return new user creation page for the project admin, where the project admin can create new users
    by providing username, password and email.
    """
    return render(request, 'projects/user_management.html')


@user_passes_test(lambda u: u.groups.filter(name='Project Admin').exists(), login_url='/projects/user_dashboard')
@login_required(login_url='/accounts/login')
def admin_projects_edit_view(request, project_name):
    """
    Return the (specific) project admin page which contain links to Info, Members, Project Metadata, Custom MD Field
    """
    return render(request, "projects/project_admin_page.html", {'project_name': project_name})


@user_passes_test(lambda u: u.groups.filter(name='Project Admin').exists(), login_url='/projects/user_dashboard')
@login_required(login_url='/accounts/login')
def admin_projects_info_view(request, prj_name):
    """
    Return project info page where the project admin can add some information about the project
    """
    try:
        pr_inst = Project.objects.get(project_name=prj_name)
        info = pr_inst.info
        return render(request, 'projects/project_info.html', {'project_name': prj_name, 'info': info})
    except ObjectDoesNotExist:
        return HttpResponse('The project object does not exist')


@user_passes_test(lambda u: u.groups.filter(name='Project Admin').exists(), login_url='/projects/user_dashboard')
@login_required(login_url='/accounts/login')
def admin_projects_edit_info(request, prj_name):
    """
    Return project info page where the project admin can edit project information, only text
    """
    get_project = get_object_or_404(Project, project_name=prj_name)
    if request.method == 'POST':
        project_edit_form = ProjectInfoForm(request.POST, instance=get_project)
        if project_edit_form.is_valid():
            project_edit_form.save()
            return redirect('/projects/admin')
        else:
            error = True
            project_edit_form.fields['admin'] = forms.ModelChoiceField(User.objects.filter(username=request.user))
            return render(request, 'projects/project_edit_info.html',
                          {'project_edit_form': project_edit_form, 'error': error, 'project_name': prj_name})
    else:
        project_edit_form = ProjectInfoForm(initial={'project_name': prj_name, 'admin': request.user},
                                            instance=get_project)
        project_edit_form.fields['admin'] = forms.ModelChoiceField(User.objects.filter(username=request.user))
        return render(request, 'projects/project_edit_info.html',
                      {'project_edit_form': project_edit_form, 'project_name': prj_name})


@user_passes_test(lambda u: u.groups.filter(name='Project Admin').exists(), login_url='/projects/user_dashboard')
@login_required(login_url='/accounts/login')
def admin_projects_add_member(request, prj_name):
    """
    Return ProjectMemberForm(page) where project admin can add Users to the project, which he/she has created using User
    Management
    """
    if request.method == 'POST':
        project_member_form = ProjectMemberRoleForm(request.POST)
        if project_member_form.is_valid():
            project_member_form.save()
            return redirect('/projects/admin')
        else:
            error = True
            return render(request, 'projects/project_add_member.html',
                          {'project_member_form': project_member_form, 'error': error, 'project_name': prj_name})
    else:
        project_member_form = ProjectMemberRoleForm()
        return render(request, 'projects/project_add_member.html',
                      {'project_member_form': project_member_form, 'project_name': prj_name})


@user_passes_test(lambda u: u.groups.filter(name='Project Admin').exists(), login_url='/projects/user_dashboard')
@login_required(login_url='/accounts/login')
def admin_projects_edit_member(request, prj_name, member):
    """
    Return ProjectMemberForm(page) where project admin can edit the member role in a particular project
    """
    prj_inst = Project.objects.get(project_name=prj_name)
    mem_inst = User.objects.get(username=member)
    get_prj = get_object_or_404(ProjectMemberRole, project=prj_inst, member=mem_inst)
    if request.method == 'POST':
        project_member_edit_form = ProjectMemberRoleForm(request.POST, instance=get_prj)
        if project_member_edit_form.is_valid():
            project_member_edit_form.save()
            return redirect('/projects/admin')
        else:
            error = True
            return render(request, 'projects/project_edit_member.html',
                          {'project_member_edit_form': project_member_edit_form, 'error': error})
    else:
        project_member_edit_form = ProjectMemberRoleForm(initial={'project': prj_inst, 'member': mem_inst},
                                                         instance=get_prj)
        return render(request, 'projects/project_edit_member.html',
                      {'project_member_edit_form': project_member_edit_form, 'project_name': prj_name,
                       'member_name': member})


@user_passes_test(lambda u: u.groups.filter(name='Project Admin').exists(), login_url='/projects/user_dashboard')
@login_required(login_url='/accounts/login')
def list_project_members(request, prj_name):
    """
    List the members of the project
    """
    try:
        prj_inst = Project.objects.get(project_name=prj_name)
        lst_mem_inst = ProjectMemberRole.objects.filter(project=prj_inst.id)
        return render(request, 'projects/project_list_members.html', {'project_name': prj_name,
                                                                      'lst_members': lst_mem_inst})
    except ObjectDoesNotExist:
        return HttpResponse('The project object does not exist')


@login_required(login_url='/accounts/login')
def project_info_view(request, prj_name):
    """
    Return project info page for the members of the project, they can't edit anything here.
    """
    try:
        pr_inst = Project.objects.get(project_name=prj_name)
        info = pr_inst.info
        return render(request, 'projects/display_project_info.html', {'project_name': prj_name, 'info': info})
    except ObjectDoesNotExist:
        return HttpResponse('The project object does not exist')






