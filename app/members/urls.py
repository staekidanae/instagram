from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'members'
urlpatterns = [
    # path('', views.index),
    path('login/', views.login_view, name='login'),
    # path('<int:pk>/', views.post_detail, name='post_detail')
]
