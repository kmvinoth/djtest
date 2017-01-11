from django.shortcuts import render, HttpResponse
from django.core.exceptions import FieldError
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Project


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
        return render(request, 'projects/project_admin.html')
    else:
        return render(request, 'projects/project_member.html')

"""
Return admin projects page to the user, who has the role "ADMIN" and can perform project
administration activities on individual project.

"""


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


@login_required(login_url='/accounts/login')
def user_mgmt(request):
    return render(request, 'projects/user_management.html')


@login_required(login_url='/accounts/login')
def admin_projects_edit_view(request):
    pass







