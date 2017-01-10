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
    url(r'^admin/\w+$', views.project_admin_page_view, name='project_admin_page'),
    url(r'^admin/\w+/user_mgmt$', views.user_mgmt, name='user_mgmt'),

]
