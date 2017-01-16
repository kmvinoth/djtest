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

# Better to use @permission required decorator to avoid code repetition, with a message permission denied
# @permission required decorator cannot be used as such for the default django User model.
#  see ref: https://docs.djangoproject.com/en/1.8/topics/auth/default/#topic-authorization


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


@login_required(login_url='/accounts/login')
def admin_projects_edit_view(request):
    pass







