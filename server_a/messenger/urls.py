from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_message/', views.update_message, name='update_message'),
]
