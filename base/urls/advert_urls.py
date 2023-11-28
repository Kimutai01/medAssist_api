from django.urls import path
from base.views import advert_views as views

urlpatterns = [
    path('', views.getAdverts, name='news'),
    path('create/', views.createAdvert, name='create-new'),
    path('upload/', views.uploadImage, name='image-upload'),
    path('<str:pk>/', views.getAdvert, name='new'),
    path('update/<str:pk>/', views.updateAdvert, name='update-new'),
    path('delete/<str:pk>/', views.deleteAdvert, name='delete-new'),

]
