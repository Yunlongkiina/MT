from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('search_form/', views.search_form, name='search_form'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('news_visual/', views.news_visual, name='news_visual'),
    path('post_detail/(^?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    path('cv/', views.cv, name='cv')
]
