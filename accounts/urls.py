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
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    url(r'^$', views.home),

    url(r'^login$', auth_views.login, {'template_name': 'accounts/login.html', 'extra_context': {'next': 'check'}},
        name='auth_login'),

    url(r'^forgot_pwd$', auth_views.password_reset),

    url(r'^check$', views.check_auth, name='check'),

    url(r'^password_change$', auth_views.password_change, {'template_name': 'accounts/password_change.html',
        'post_change_redirect': 'password_change_done'}, name='password_change'),

    url(r'^password_change_done$', auth_views.password_change_done, {'template_name': 'accounts/password_change_done.html'},
        name='password_change_done'),

    url(r'^logout$', auth_views.logout, {'template_name': 'accounts/logout.html'}, name='logout'),

]
