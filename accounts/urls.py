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
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^register$', views.user_registration, name='user_registration'),

    url(r'^register_success$', views.user_registration_success, name='user_registration_success'),

    url(r'^login$', auth_views.login, {'template_name': 'accounts/login.html'}, name='auth_login'),

    url(r'^profile$', views.update_profile, name='profile'),

    # Start the local mail server before executing this url
    # else you get connection refused error
    url(r'^password_reset$', auth_views.password_reset,
        {'template_name': 'accounts/password_reset.html', 'email_template_name': 'accounts/password_reset_email.html',
         'subject_template_name': 'accounts/password_reset_subject.txt',
         'post_reset_redirect': 'accounts:password_reset_done'}, name='password_reset'),

    url(r'^password_reset_done$', auth_views.password_reset_done,
        {'template_name': 'accounts/password_reset_done.html'}, name='password_reset_done'),

    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm,
        {'template_name': 'accounts/password_reset_confirm.html',
         'post_reset_redirect': 'accounts:password_reset_complete'}, name='password_reset_confirm'),

    url(r'^password_reset_complete$', auth_views.password_reset_complete,
        {'template_name': 'accounts/password_reset_complete.html'}, name='password_reset_complete'),

    url(r'^check$', views.check_auth, name='check'),

    url(r'^password_change$', auth_views.password_change, {'template_name': 'accounts/password_change.html',
        'post_change_redirect': 'accounts:password_change_done'}, name='password_change'),

    url(r'^password_change_done$', auth_views.password_change_done,
        {'template_name': 'accounts/password_change_done.html'}, name='password_change_done'),

    url(r'^logout$', auth_views.logout, {'template_name': 'accounts/logout.html'}, name='logout'),

]
