from django.conf.urls import url #importing Django's function url
from . import views

urlpatterns = [
    # ^$ : go to site with empty string https://{DOMAIN}.com/
    # name : name of the URL that will be used to identify the view
    url(r'^$', views.post_list, name='post_list'),
]