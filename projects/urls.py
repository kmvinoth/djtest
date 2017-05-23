"""

This module contains the urls for projects app. In future, add any Url related to projects app here.

"""
from django.conf.urls import url
from projects import views

urlpatterns = [
    url(r'^user_dashboard$', views.project_member_view, name='user_dashboard'),
    url(r'^admin$', views.admin_projects_view, name='admin_projects'),
    url(r'^admin/user_mgmt$', views.user_mgmt, name='user_mgmt'),
    # Passing the project name as an argument to the view function
    url(r'^admin/(\w+)$', views.admin_projects_edit_view, name='admin_projects_edit'),
    url(r'^admin/(\w+)/info$', views.admin_projects_info_view, name='admin_projects_info'),
    url(r'^admin/(\w+)/edit_info$', views.admin_projects_edit_info, name='admin_projects_edit_info'),
    url(r'^admin/(\w+)/lst_member$', views.list_project_members, name='list_project_members'),
    url(r'^admin/(\w+)/add_member$', views.admin_projects_add_member, name='admin_projects_add_member'),
    url(r'^admin/(\w+)/(\w+)$', views.admin_projects_edit_member, name='admin_projects_edit_member'),
    url(r'^(\w+)/info$', views.project_info_view, name='projects_info'),
    url(r'^\w+/metadata$', views.project_info_view, name='projects_metadata'),
    # url(r'^\w+/members$', views.project_view, name='projects_members'),

]
