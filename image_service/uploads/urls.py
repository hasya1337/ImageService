from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_upload_form, name='image_upload_form'),
    path('image/<int:pk>/', views.image_view, name='image_view'),
    path('api/upload/', views.api_image_upload, name='api_image_upload'),
]
