"""djtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
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

Application and instance namespace
     See the below link for application name space and instance namespace
     https://docs.djangoproject.com/en/1.8/topics/http/urls/#term-application-namespace
     instance namespace : This identifies a specific instance of an application.
     Instance namespaces should be unique across your entire project.
     However, an instance namespace can be the same as the application namespace.
     This is used to specify a default instance of an application.
     For example, the default Django admin instance has an instance namespace of 'admin'.
"""

from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin


from accounts import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls', app_name='accounts', namespace='accounts')),
    url(r'^projects/', include('projects.urls', app_name='projects', namespace='projects')),
]
# for Django debug toolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
