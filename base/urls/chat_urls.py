from django.urls import path
from base.views import news_views as views

urlpatterns = [
    path('', views.getNews, name='news'),
]
