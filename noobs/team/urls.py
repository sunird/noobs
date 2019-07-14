from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles',views.articles,name='articles'),
    path('art_detail',views.art_detail,name='art_detail'),
]
