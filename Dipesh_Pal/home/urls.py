from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.homepage, name="home"),
    path('create/', views.article_create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
    url(r'^(?P<slug>[\w-]+)/edit/', views.article_update, name="post_edit"),
    url(r'^(?P<slug>[\w-]+)/delete/', views.article_delete, name="delete_post"),
]
