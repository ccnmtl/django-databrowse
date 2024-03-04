from django.urls import re_path
import django_databrowse

urlpatterns = [
    re_path(r'^(.*)', django_databrowse.site.root),
]
