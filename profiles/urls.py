from django.contrib.auth import views
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import path
from .views import *

app_name = 'profiles'

urlpatterns = [
    path('profile/<str:username>', profile_view, name='profile'),
    path('profile/saved/', saved_list_view, name='saved'),
    path('profile/archive/', archive_list_view, name='archive'),
    path('profile_update/<int:pk>', profile_update_view, name='profile_update'),
]
