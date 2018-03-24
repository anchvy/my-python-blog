from django.conf.urls import url #importing Django's function url
from . import views

urlpatterns = [
    # ^$ : go to site with empty string https://{DOMAIN}.com/(post)
    # name : name of the URL that will be used to identify the view
    url(r'^$|^post$', views.post_list, name='post_list'),
    # transfer it to a view as a variable called pk
    # d : only decimal
    # https://{DOMAIN}.com/post/5/
    url(r'^post/(?P<pk>\d)+(/)?$', views.post_detail, name='post_detail'),
	# url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/new$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit+(/)?$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/delete+(/)?$', views.post_delete, name='post_delete'),
]