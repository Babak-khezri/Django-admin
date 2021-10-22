from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreateForm
from .models import User
from profiles.models import Profile
from . import otp_handler
from django.http import JsonResponse

# Create your views here.


def login_view(request):
    form = AuthenticationForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    form = UserCreateForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password2']
        email = form.cleaned_data['email']
        user = User.objects.create_user(username=username, email=email, password=password)
        profile = Profile.objects.create(user=user)
        profile.name = form.cleaned_data['name']
        profile.save()
        login(request, user)
        return redirect('/')
    return render(request, 'account/signup.html', {'form': form})


def forget_password_view(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            user.otp = otp_handler.create_otp()
            otp_handler.send_otp(user.email,user.otp)
            user.save()
            request.session['user_email'] = user.email
            return redirect('account:verify_otp')
        except:
            error = 'User not found !!!'
            context['error'] = error
    return render(request, 'account/forget_password.html',context)


def verify_otp_view(request):
    context = {}
    email = request.session.get('user_email')
    user = get_object_or_404(User,email=email)
    if request.method == 'POST':
        otp = request.POST.get('otp')
        if otp_handler.check_otp_expiration(user.email):
            if(user.otp == int(otp)):
                return redirect('account:reset_password')
            else:
                context['error'] = "Code is not valid !"
        else:
            context['error'] = "The code is expired !"   
    return render(request, 'account/verify_otp.html',context)


def resend_code_view(request):
    if request.is_ajax():
        email = request.session.get('user_email')
        try:
            user = get_object_or_404(User, email=email)
            user.otp = otp_handler.create_otp()
            user.save()
            print(user.otp)
            return JsonResponse({}, status=200)
        except User.DoesNotExist:
            return redirect('account:forget_password')


def reset_password_view(request):
    context = {}
    email = request.session.get('user_email')
    user = get_object_or_404(User,email=email)
    if request.method == 'POST':
        password = request.POST.get('password1')
        user.set_password(password)
        user.save()
        login(request, user)
        request.session.clear()
        return redirect('/')
    return render(request, 'account/reset_password.html',context)


def search_account(request):
    keyword = request.POST.get('search')
    accounts = [account for account in User.objects.all()
                if keyword in account.email.split('@')[0]
                or keyword in account.profile.name
                or keyword in account.profile.bio]
    return render(request, 'account/account_list.html', {'accounts': accounts})


def followers_list(request, username):
    user = get_object_or_404(User, username=username)
    accounts = [account for account in user.followers.all()]
    return render(request, 'account/account_list.html', {'accounts': accounts})


def following_list(request, username):
    user = get_object_or_404(User, username=username)
    accounts = [account for account in user.following.all()]
    return render(request, 'account/account_list.html', {'accounts': accounts})


def request_account(request, username):
    user = get_object_or_404(User, username=username)
    user.requests.add(request.user)
    user.save()
    return redirect('profiles:profile', user.username)


def accept_request(request, username):
    user = get_object_or_404(User, username=username)
    request.user.requests.remove(user)
    user.following.add(request.user)
    return redirect('profiles:profile', user.username)


def cancel_request(request, username):
    user = get_object_or_404(User, username=username)
    user.requests.remove(request.user)
    user.save()
    return redirect('profiles:profile', user.username)


def request_list(request):
    return render(request, 'account/request_list.html')


def follow_account(request, username):
    user = get_object_or_404(User, username=username)
    request.user.following.add(user)
    return redirect('profiles:profile', user.username)


def unfollow_account(request, username):
    user = get_object_or_404(User, username=username)
    request.user.following.remove(user)
    return redirect('profiles:profile', user.username)
