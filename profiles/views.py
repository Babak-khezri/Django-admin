from django.shortcuts import render, get_object_or_404, redirect
from post.models import Post
from django.db.models import Q
from .forms import ProfileForm
from .models import Profile
from account.models import User

# Create your views here.


def profile_update_view(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    form = ProfileForm(request.POST or None, instance=profile)
    user = profile.user
    if request.method == 'POST' and form.is_valid():
        username = form.clean_username()
        user.username = username
        user.save()
        form.save()
        return redirect('profiles:profile', user.username)
    return render(request, 'profiles/profile_update.html',{'form':form})


def saved_list_view(request):
    user = request.user
    posts = reversed(user.saved.all())
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'profiles/saved_list.html', context)


def archive_list_view(request):
    user = request.user
    posts = reversed(Post.objects.filter(Q(user=user) & Q(is_archived=True)))
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'profiles/archive_list.html', context)


def profile_view(request, username):

    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(Q(user=user) & Q(
        is_archived=False)).order_by("-date")
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'profiles/profile.html', context)
