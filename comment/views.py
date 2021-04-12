from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from post.models import Post
from .models import Comment
from account.models import User
# Create your views here.


def add_comment_view(request, pk):
    if request.method == 'POST':
        user = request.user
        post = get_object_or_404(Post, pk=pk)
        text = request.POST.get('text')
        comment = Comment.objects.create(user=user, post=post, text=text)
        comment.save()
    return redirect("post:post_detail", post.pk)


def replay_comment_view(request, post_pk, comment_pk):
    if request.method == 'POST':
        user = request.user
        post = get_object_or_404(Post, pk=post_pk)
        comment = get_object_or_404(Comment, pk=comment_pk)
        text = request.POST.get('text')
        replay = Comment.objects.create(
            user=user, parent=comment, post=post, text=text)
        replay.save()
    return redirect("post:post_detail", post.pk)


def like_comment_view(request, comment_pk):
    user = request.user
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.likes.add(user)
    if user in comment.dislikes.all():
        comment.dislikes.remove(user)
    return redirect('post:post_detail', comment.post.pk)


def dislike_comment_view(request,comment_pk):
    user = request.user
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.dislikes.add(user)
    if user in comment.likes.all():
        comment.likes.remove(user)
    return redirect('post:post_detail', comment.post.pk)
