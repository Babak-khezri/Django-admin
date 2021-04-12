from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from account.models import User
from .mixins import FormValidMixin
# Create your views here.


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post/post_detail.html', {'post': post})


class PostCreateView(LoginRequiredMixin, FormValidMixin, CreateView):
    model = Post
    fields = ['image_1','image_2','image_3', 'text']
    template_name = 'post/post_create.html'


def like_post(request, username, post_pk):
    if request.is_ajax():
        user = get_object_or_404(User, username=username)
        post = get_object_or_404(Post, pk=post_pk)
        if user == request.user:
            post.likes.add(user)
            return JsonResponse({},status=200)


def unlike_post(request, username, post_pk):
    if request.is_ajax():
        user = get_object_or_404(User, username=username)
        post = get_object_or_404(Post, pk=post_pk)
        if user == request.user:
            post.likes.remove(user)
            return JsonResponse({},status=200)

def save_post(request, username, post_pk):
    if request.is_ajax():
        user = get_object_or_404(User, username=username)
        post = get_object_or_404(Post, pk=post_pk)
        if user == request.user:
            post.saves.add(user)
            return JsonResponse({},status=200)


def unsave_post(request, username, post_pk):
    if request.is_ajax():
        user = get_object_or_404(User, username=username)
        post = get_object_or_404(Post, pk=post_pk)
        if user == request.user:
            post.saves.remove(user)
            return JsonResponse({},status=200)


def archive_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.user:
        post.is_archived = True
        post.save()
    return redirect("account:profile",post.user.username)

def show_on_profile_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.user:
        post.is_archived = False
        post.save()
    return redirect("account:profile",post.user.username)


def delete_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.user:
        post.delete()
    return redirect("account:profile",post.user.username)
