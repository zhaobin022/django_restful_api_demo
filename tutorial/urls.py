"""tutorial URL Configuration

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
from django.conf.urls import url, include
from rest_framework import routers
from quickstart import views
from django.conf.urls import include


# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

from snippets.views import SnippetViewSet, api_root
from quickstart.views import UserViewSet
from rest_framework import renderers

from django.conf.urls import url, include
from snippets import views as snippets_views
from quickstart import views as user_views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', snippets_views.SnippetViewSet)
router.register(r'users', user_views.UserViewSet)







urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    # url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]