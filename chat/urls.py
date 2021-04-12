from django.urls import path
from .views import *

app_name = 'chat'
urlpatterns = [
    path('direct_list/<str:username>/',direct_list_view,name='direct_list'),
    path('direct/<str:username>/',direct_view,name='direct'),
    path('send_message/<str:username>/',send_message_view,name='send_message'),
    path('delete_message/<int:pk>/',delete_message_view,name='delete_message'),

]
