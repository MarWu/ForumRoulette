from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile_picture/', views.change_profile_picture, name='profile_picture'),
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
]
