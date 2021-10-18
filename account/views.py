from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreateForm
from .models import User
from profiles.models import Profile


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
