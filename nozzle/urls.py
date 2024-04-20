from django import views
from django.contrib import admin
from django.urls import include, path
from nozzle.views import home, DownloadPDFView

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('download/pdf/<str:file_path>/', DownloadPDFView.as_view(), name='download_pdf'),
]