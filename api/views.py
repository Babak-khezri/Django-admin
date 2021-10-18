# from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import (UserSerializer,
                         ProfileSerializer,
                         PostSerializer,
                         StorySerializer,
                         CommentSerializer,
                         HighlightSerializer)
from account.models import User
from profiles.models import Profile
from post.models import Post
from story.models import Story, Highlight
from comment.models import Comment
# Create your views here.


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "username"


class ProfileList(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class StoryList(ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class StoryDetail(RetrieveAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class HighlightList(ListAPIView):
    queryset = Highlight.objects.all()
    serializer_class = HighlightSerializer


class HighlightDetail(RetrieveAPIView):
    queryset = Highlight.objects.all()
    serializer_class = HighlightSerializer



class CommentList(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
