from django.urls import path
from .views import *

app_name = 'post'
urlpatterns = [
    path('detail/<int:pk>', post_detail, name='post_detail'),
    path('new_post/', PostCreateView.as_view(), name='new_post'),
    path('like_post/<str:username>/<str:post_pk>',like_post,name='like_post'),
    path('unlike_post/<str:username>/<str:post_pk>',unlike_post,name='unlike_post'),
    path('save_post/<str:username>/<str:post_pk>',save_post,name='save_post'),
    path('unsave_post/<str:username>/<str:post_pk>',unsave_post,name='unsave_post'),
    path('archive_post/<int:pk>',archive_post,name='archive_post'),
    path('show_on_profile/<int:pk>',show_on_profile_post,name='show_on_profile'),
    path('delete_post/<int:pk>',delete_post,name='delete_post'),
    
]
