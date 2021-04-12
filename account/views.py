from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls.base import reverse
from .forms import SignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from .models import User
from post.models import Post
from django.db.models import Q


# Create your views here.


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    user_list = [user.username for user in User.objects.all()]
    users = " ".join(user_list)
    email_list = [user.email for user in User.objects.all()]
    emails = " ".join(email_list)
    print(users)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    context = {
        'form': form,
         'users': users,
         'emails': emails,
    }
    return render(request, 'account/signup.html', context)


def profile_view(request, username):

    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(Q(user=user) & Q(
        is_archived=False)).order_by("-date")
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'account/profile.html', context)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'image', 'email', 'name', 'bio',
              'is_private', 'birth', 'gender', 'dark_mode']
    template_name = 'account/profile_update.html'

    def get_success_url(self):
        return reverse('account:profile', kwargs={'username': self.object.username})


def search_account(request):
    keyword = request.POST.get('search')
    accounts = [account for account in User.objects.all()
                if keyword in account.email.split('@')[0]
                or keyword in account.name
                or keyword in account.bio]
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
    return redirect('account:profile', user.username)


def accept_request(request, username):
    user = get_object_or_404(User, username=username)
    request.user.requests.remove(user)
    user.following.add(request.user)
    return redirect('account:profile', user.username)


def cancel_request(request, username):
    user = get_object_or_404(User, username=username)
    user.requests.remove(request.user)
    user.save()
    return redirect('account:profile', user.username)


def request_list(request):
    return render(request, 'account/request_list.html')


def follow_account(request, username):
    user = get_object_or_404(User, username=username)
    request.user.following.add(user)
    return redirect('account:profile', user.username)


def unfollow_account(request, username):
    user = get_object_or_404(User, username=username)
    request.user.following.remove(user)
    return redirect('account:profile', user.username)


def saved_list_view(request):
    user = request.user
    posts = reversed(user.saved.all())
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'account/saved_list.html', context)


def archive_list_view(request):
    user = request.user
    posts = reversed(Post.objects.filter(Q(user=user) & Q(is_archived=True)))
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'account/archive_list.html', context)
