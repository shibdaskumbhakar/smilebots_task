from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comments, Like, CommentLike
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'id')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'titel', 'description')


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'user', 'post', 'comment')


class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'user', 'post', 'likes')
