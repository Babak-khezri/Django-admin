from django.urls import path
from .views import *

app_name = 'comment'

urlpatterns = [
    path('add_comment/<int:pk>',add_comment_view,name='add_comment'),
    path('replay_comment/<int:post_pk>/<int:comment_pk>',replay_comment_view,name='replay_comment'),
    path('like_comment/<int:comment_pk>',like_comment_view,name='like_comment'),
    path('dislike_comment/<int:comment_pk>',dislike_comment_view,name='dislike_comment'),
]
