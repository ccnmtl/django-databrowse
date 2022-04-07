from django.conf.urls import url
from django_databrowse import views

# Note: The views in this URLconf all require a 'models' argument,
# which is a list of model classes (*not* instances).

urlpatterns = [
    url(r'^([^/]+)/([^/]+)/fields/(\w+)/$', views.choice_list),
    url(r'^([^/]+)/([^/]+)/fields/(\w+)/(.*)/$', views.choice_detail),
]
