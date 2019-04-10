
from django.conf.urls import url
from django.contrib import admin
from.import views
app_name= "places"
urlpatterns = [
    url(r'^$',views.article_list,name="list"),
    url(r'^create/$',views.article_create,name="create"),
    url(r'^(?P<pk>[\w-]+)/$',views.article_details,name="details"),
    url(r'^category/(?P<pk>[\w-]+)/$', views.show_category, name='category'),
    
    url(r'^tag/(?P<tag_slug>[\w-]+)/$',views.article_list,name='post_list_by_tag'),






]
