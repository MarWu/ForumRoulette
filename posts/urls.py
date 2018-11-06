from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('popular/', views.popular, name='popular'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('create/', views.create_post, name='create'),
    path('<int:post_id>/vote/', views.vote, name='vote'),
    path('<int:post_id>/vote/<int:is_down_vote>/', views.vote, name='vote'),
    path('<int:post_id>/down_vote/', views.down_vote, name='down_vote'),
    path('<int:comment_id>/vote/comment/<int:is_down_vote>', views.vote_comment, name='vote_comment'),
    path('<int:post_id>/comment/', views.create_comment, name='comment'),
    path('random/', views.random_comment, name='random'),
]
