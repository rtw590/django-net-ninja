from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list),
    path(r'^(?P<slug>[\w-]+)/$', views.article_details)
]
