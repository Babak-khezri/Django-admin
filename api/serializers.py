from rest_framework import serializers
from account.models import User
from profiles.models import Profile
from post.models import Post
from story.models import Story, Highlight
from comment.models import Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = "__all__"


class HighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Highlight
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
