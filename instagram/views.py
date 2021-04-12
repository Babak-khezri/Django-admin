from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from post.models import Post
from account.models import User
from django.db.models import Q
import random
from story.models import Story
# Create your views here.


@login_required
def home_view(request):
    user = request.user  # get accounts
    accounts_list = request.user.following.all()
    accounts , posts = stories_and_posts(accounts_list,user)
    suggestions = [suggest_user for suggest_user in User.objects.all() if suggest_user not in user.following.all() and suggest_user != user]
    context = {
        'suggestions': suggestions,
        'posts': posts,
        'accounts': accounts,
    }
    return render(request, 'instagram/home.html', context)

def stories_and_posts(accounts_list,user):
    posts = []  # get posts
    posts.extend(Post.objects.filter(Q(user=user) & Q(is_archived=False)))
    for account in accounts_list:
        posts.extend(Post.objects.filter(Q(user=account) & Q(is_archived=False)))
    posts.sort(key=lambda x: x.date)
    posts.reverse()

    accounts = [user]  if user.stories.active() else []
    for account in accounts_list:
        if account.stories.active():
            accounts.append(account)
    return accounts, posts


def explorer_view(request):
    accounts = User.objects.filter(is_private=False)
    posts = []
    for account in accounts:
        posts.extend(Post.objects.filter(Q(user=account) & Q(is_archived=False)))
    random.shuffle(posts)
    return render(request, 'instagram/explorer.html', {'posts': posts})
