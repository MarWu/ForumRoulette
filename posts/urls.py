from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('create/', views.create_post, name='create'),
    path('<int:post_id>/vote/', views.vote, name='vote'),
    path('<int:post_id>/comment/', views.create_comment, name='comment'),
    path('random/', views.random_comment, name='random'),
]
