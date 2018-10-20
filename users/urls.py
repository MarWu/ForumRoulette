from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
]
