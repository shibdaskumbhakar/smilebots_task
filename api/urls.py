from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UserViewSet, PostViewSet, LikeViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('post', PostViewSet)
router.register('comment', CommentViewSet)
router.register('like', LikeViewSet)


urlpatterns = [
    path('', include(router.urls)),

]
