from django.urls import path

from .views import *

urlpatterns = [
    path('', coordConv, name="coordConv"),
    path('Download/', coordExport, name="homepagecoordExport)"),
]