from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Post, Comments, Like
from rest_framework.authentication import TokenAuthentication
from .serializers import UserSerializer, PostSerializers, CommentSerializers, LikeSerializers
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    authentication_classes = (TokenAuthentication, )


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializers
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializers
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)
