"""Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.urls import path
from django.contrib import admin

from rest_framework import routers
from App import views
from App.models import WordFrequency


router = routers.DefaultRouter()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^search/', views.WordViewSet.as_view()),
    path('words/', views.WordCreateSongsView.as_view(), name="words-list-create"),
    path('words/<str:pk>/', views.WordsDetailView.as_view(), name="words-detail"),
]
