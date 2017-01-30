"""website URL Configuration

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

# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from website.views import current_datetime
from website.views import universite
from website.views import ceyrekAltin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('jobs.urls')),
    url(r'^mainWeb.py/', include('jobs.urls')),
    url(r'^time/$', current_datetime),
    url(r'^universite/',universite),
    url(r'^ceyrek_altin/', ceyrekAltin)

]
