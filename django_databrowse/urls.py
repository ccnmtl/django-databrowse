from django.urls import re_path
from django_databrowse import views

# Note: The views in this URLconf all require a 'models' argument,
# which is a list of model classes (*not* instances).

urlpatterns = [
    re_path(r'^([^/]+)/([^/]+)/fields/(\w+)/$', views.choice_list),
    re_path(r'^([^/]+)/([^/]+)/fields/(\w+)/(.*)/$', views.choice_detail),
]
