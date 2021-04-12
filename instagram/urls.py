from django.urls import path
from .views import *

app_name = 'instagram'
urlpatterns = [
    path('', home_view, name='home'),
    path('explorer',explorer_view, name='explorer'),
]
