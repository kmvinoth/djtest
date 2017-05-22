"""
This module contains the urls for accounts app. In future, add any Url related to accounts app here.

The Views for login, password_reset, password_change, logout are used from the builtin Django auth views and the
corresponding templates have been provided in the templates folder "accounts/templates/accounts"
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
