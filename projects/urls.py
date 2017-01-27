""" djtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from projects import views

urlpatterns = [
    url(r'^user_dashboard$', views.project_member_view, name='user_dashboard'),
    url(r'^admin$', views.admin_projects_view, name='admin_projects'),
    url(r'^admin/user_mgmt$', views.user_mgmt, name='user_mgmt'),
    # Passing the project name as an argument to the view function
    url(r'^admin/(\w+)$', views.admin_projects_edit_view, name='admin_projects_edit'),
    url(r'^admin/\w+/add_info$', views.admin_projects_add_info, name='admin_projects_add_info'),
    url(r'^admin/\w+/add_member$', views.admin_projects_add_member, name='admin_projects_add_member'),

]
