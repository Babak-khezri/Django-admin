from django.urls import path
from .views import *

app_name = 'api'
urlpatterns = [
    path("users/",UserList.as_view(),name="users"),
    path("users/<str:username>",UserDetail.as_view(),name="user_detail"),
    path("profiles/",ProfileList.as_view(),name="profiles"),
    path("profiles/<int:pk>",ProfileDetail.as_view(),name="profile_detail"),
    path("posts/",PostList.as_view(),name="posts"),
    path("posts/<int:pk>",PostDetail.as_view(),name="post_detail"),
    path("stories/",StoryList.as_view(),name="stories"),
    path("stories/<int:pk>",StoryDetail.as_view(),name="story_detail"),
    path("stories/",StoryList.as_view(),name="stories"),
    path("stories/<int:pk>",StoryDetail.as_view(),name="story_detail"),
    
]
