from django.contrib.auth import views
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import path
from .views import *

app_name = 'account'
urlpatterns = [
    path('login',login_view,name='login'),
    path('signup',signup_view,name='signup'),
    path('logout',logout_view,name='logout'),
    path('profile/<str:username>',profile_view,name='profile'),
    path('profile/saved/',saved_list_view,name='saved'),
    path('profile/archive/',archive_list_view,name='archive'),
    path('profile_update/<int:pk>',ProfileUpdateView.as_view(),name='profile_update'),
    path('search_account/',search_account,name='search_account'),
    path('followers_list/<str:username>',followers_list,name='followers_list'),
    path('following_list/<str:username>',following_list,name='following_list'),
    path('follow_account/<str:username>',follow_account,name='follow_account'),
    path('unfollow_account/<str:username>',unfollow_account,name='unfollow_account'),
    path('request_account/<str:username>',request_account,name='request_account'),
    path('accept_request/<str:username>',accept_request,name='accept_request'),
    path('cancel_request/<str:username>',cancel_request,name='cancel_request'),
    path('request_list',request_list,name='request_list'),
    path('password_change/',views.PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done',views.PasswordChangeDoneView.as_view(),name='password_change_done'),
]
