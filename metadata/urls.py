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
    url(r'^(\w+)/add_project_metadata$', views.add_project_metadata, name='add_project_metadata'),
    url(r'^(\w+)/add_custom_md_attributes$', views.add_custom_md_attributes, name='add_custom_md_attributes'),
    url(r'^(\w+)/create_deposit$', views.create_deposit_session, name='create_deposit_session'),
    url(r'^(\w+)/member_md_dashboard$', views.member_metadata_view, name='member_metadata_view'),
    url(r'^(\w+)/add_deposit_metadata$', views.add_deposit_metadata, name='add_deposit'),
    # url(r'^(\w+)/lst_deposit$', views.lst_deposit_session, name='lst_deposit'),
    url(r'^(\w+)/(\w+)/edit_deposit$', views.edit_deposit_session, name='edit_deposit'),


    url(r'^(\w+)/(\w+)/create_data_object$', views.create_dataobject, name='create_data_object'),
    url(r'^(\w+)/(\w+)/add_dataobject_metadata$', views.add_dataobject_metadata, name='add_dataobject'),



]
