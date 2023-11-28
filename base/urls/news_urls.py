from django.urls import path
from base.views import news_views as views

urlpatterns = [
    path('', views.getNews, name='news'),
    path('create/', views.createNew, name='create-new'),
    path('upload/', views.uploadImage, name='image-upload'),
    path('latest/', views.getOneLatestNew, name='latest-new'),
    path('otherlatest/', views.getNextFourLatestNews, name='other-latest-new'),
    path('<str:pk>/', views.getNew, name='new'),
    path('update/<str:pk>/', views.updateNew, name='update-new'),
    path('delete/<str:pk>/', views.deleteNew, name='delete-new'),

]
