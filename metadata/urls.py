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
from metadata import views

urlpatterns = [
    url(r'^(\w+)/project_metadata$', views.project_metadata, name='project_metadata'),
    url(r'^(\w+)/add_project_metadata$', views.add_project_metadata, name='add_project_metadata'),
    url(r'^(\w+)/edit_project_metadata$', views.admin_projects_edit_project_metadata, name='edit_project_metadata'),
]
