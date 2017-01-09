from django.shortcuts import render


def project_member_view(request):

    # If the user is in group Project Admin (created by portal administrator),
    # the user get's the Admin (project admin) link in his page,
    # so that he can do admin activities for the specified project
    # else the user gets the norma project member view
    try:
        member_inst = request.user.groups.filter(name='Project Admin').exists()
        return render(request, 'projects/project_admin.html')
    except PermissionError:
        return render(request, 'projects/project_member.html')
