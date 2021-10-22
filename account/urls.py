from django.contrib.auth import views
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import path
from .views import *

app_name = 'account'
urlpatterns = [
    path('login/',login_view,name='login'),
    path('signup/',signup_view,name='signup'),
    path('logout/',logout_view,name='logout'),
    path('forget_password/',forget_password_view,name='forget_password'),
    path('forget_password/verify_otp/',verify_otp_view,name='verify_otp'),
    path('resend_code/',resend_code_view,name='resend_code'),
    path('forget_password/reset_password',reset_password_view,name='reset_password'),
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
