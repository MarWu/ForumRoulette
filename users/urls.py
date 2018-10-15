from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<string:username>/', views.profile, name='profile'),
]
