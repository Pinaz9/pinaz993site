"""cv URL Configuration

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
from django.contrib import admin
from django.views.generic.base import RedirectView
import pages.views

urlpatterns = [
    url(r'^references/?$', pages.views.ReferencesView.as_view(), name='references'),
    url(r'^interests/?$', pages.views.InterestView.as_view(), name='interests'),
    url(r'^experience/?$', pages.views.ExperienceView.as_view(), name='experience'),
    url(r'^skills/?$', pages.views.SkillsView.as_view(), name='skills'),
    url(r'^bio/?$', pages.views.BioView.as_view(), name='home'),
    url(r'^.*$', RedirectView.as_view(pattern_name="home"), name="go_home"),  # As in: "Go home browser, you're drunk."
    url(r'^admin/', admin.site.urls),
]
