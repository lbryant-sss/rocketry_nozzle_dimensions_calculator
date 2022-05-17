from django.contrib import admin
from django.urls import include, path
from nozzle.views import home

urlpatterns = [
    path('', home.as_view(), name='home'),
]