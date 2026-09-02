"""
URL configuration for nwbackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from nwchannels.views import NWChannelViewSet
from nwusers.views import NWUserViewSet
from nwgroups.views import NWGroupViewSet

# Channels are only defined within the scope of groups, look into this
# to make sure that all channel operations can only happen within a group
# Ex: /groups/1/channels/1/ (In order to get a channel with ID 1)
# Ex (continued): instead of doing /channels/1/
# Use this: https://github.com/alanjds/drf-nested-routers

router = DefaultRouter()
router.register(r'users', NWUserViewSet)
router.register(r'groups',NWGroupViewSet)
router.register(r'groups/channels',NWChannelViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
