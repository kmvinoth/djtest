from django.shortcuts import render, HttpResponse, redirect
from django.core.exceptions import FieldError
from django.contrib.auth.decorators import user_passes_test, login_required
from django import forms
from .models import Project, User, ProjectMemberRole
from .forms import ProjectInfoForm, ProjectMemberRoleForm


"""
Return projects page (project Dashboard) to the user after successful login.

    If the user is in group Project Admin (created by portal administrator),
    the user get's the Admin (project admin) link in his page,
    so that he can do admin activities for the specified project
    else the user gets the normal project member view.

"""


@login_required(login_url='/accounts/login')
def project_member_view(request):

    member_inst = request.user.groups.filter(name='Project Admin').exists()
    if member_inst:
        admin_prjs = Project.objects.filter(admin=request.user)
        member_prjs = ProjectMemberRole.objects.filter(member=request.user)
        return render(request, 'projects/project_admin.html', {'member_projects': member_prjs,
                                                               'admin_projects': admin_prjs})
    else:
        member_prjs = ProjectMemberRole.objects.filter(member=request.user)  # returns Queryset
        return render(request, 'projects/project_member.html', {'member_projects': member_prjs})

"""
Return admin projects page to the user, who has the role "ADMIN" and can perform project
administration activities on individual project.

"""

# Better to use @permission required decorator to avoid code repetition, with a message permission denied
# @permission required decorator cannot be used as such for the default django User model.
#  see ref: https://docs.djangoproject.com/en/1.8/topics/auth/default/#topic-authorization
# @user_passes_test decorator is slow as well because you are hitting the database


@user_passes_test(lambda u: u.groups.filter(name='Project Admin').exists(), login_url='/projects/user_dashboard')
@login_required(login_url='/accounts/login')
def admin_projects_view(request):
    try:
        admin_prjs = Project.objects.filter(admin=request.user)  # returns Queryset
        return render(request, 'projects/admin_projects.html', {'admin_projects': admin_prjs})
    except FieldError:
        return HttpResponse('Some kind of problem with a model field')

"""
Return new user creation page for the project admin, where the project admin can create new users
by providing username, password and email.
"""

# same comment as for admin_projects_view


@user_passes_test(lambda u: u.groups.filter(name='Project Admin').exists(), login_url='/projects/user_dashboard')
@login_required(login_url='/accounts/login')
def user_mgmt(request):
    return render(request, 'projects/user_management.html')


@user_passes_test(lambda u: u.groups.filter(name='Project Admin').exists(), login_url='/projects/user_dashboard')
@login_required(login_url='/accounts/login')
def admin_projects_edit_view(request, project_name):
    return render(request, "projects/project_admin_page.html", {'project_name': project_name})


@user_passes_test(lambda u: u.groups.filter(name='Project Admin').exists(), login_url='/projects/user_dashboard')
@login_required(login_url='/accounts/login')
def admin_projects_add_info(request):
    if request.method == 'POST':
        project_info_form = ProjectInfoForm(request.POST)
        if project_info_form.is_valid():
            project_info_form.save()
            return redirect('/projects/admin')
        else:
            error = True
            return render(request, 'projects/project_info.html',
                          {'project_info_form': project_info_form, 'error': error})
    else:
        project_info_form = ProjectInfoForm()
        project_info_form.fields['admin'] = forms.ModelChoiceField(User.objects.filter(username=request.user))
        return render(request, 'projects/project_info.html',
                      {'project_info_form': project_info_form})


@user_passes_test(lambda u: u.groups.filter(name='Project Admin').exists(), login_url='/projects/user_dashboard')
@login_required(login_url='/accounts/login')
def admin_projects_add_member(request):
    if request.method == 'POST':
        project_member_form = ProjectMemberRoleForm(request.POST)
        if project_member_form.is_valid():
            project_member_form.save()
            return redirect('/projects/admin')
        else:
            error = True
            return render(request, 'projects/project_add_member.html',
                          {'project_member_form': project_member_form, 'error': error})
    else:
        project_member_form = ProjectMemberRoleForm()
        return render(request, 'projects/project_add_member.html',
                      {'project_member_form': project_member_form})








