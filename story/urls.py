from django.urls import path
from .views import *

app_name = 'story'
urlpatterns = [
    path('add_story',StoryCreateView.as_view(),name='add_story'),
    path('story_list/<str:username>',story_list_view,name='story_list'),
    path('highlite_create',highlite_create_view,name='highlite_create'),
    path('highlight_story<int:pk>',highlight_story_view,name='highlight_story'),
]
