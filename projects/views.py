from django.shortcuts import render
from accounts.views import login_required


@login_required(login_url='/accounts/login')
def project_member_view(request):

    # If the user is in group Project Admin (created by portal administrator),
    # the user get's the Admin (project admin) link in his page,
    # so that he can do admin activities for the specified project
    # else the user gets the norma project member view
    member_inst = request.user.groups.filter(name='Project Admin').exists()
    if member_inst:
        return render(request, 'projects/project_admin.html')
    else:
        return render(request, 'projects/project_member.html')
