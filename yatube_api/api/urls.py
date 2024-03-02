from django.urls import include, path
from rest_framework import routers

from api.views import (PostViewSet, CommentViewSet,
                       GroupViewSet, FollowViewSet)


router_api_v1 = routers.DefaultRouter()
router_api_v1.register(
    'posts',
    PostViewSet,
    basename='posts'
)
router_api_v1.register(
    'groups',
    GroupViewSet,
    basename='groups'
)
router_api_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_api_v1.register(
    'follow',
    FollowViewSet,
    basename='follow'
)

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_api_v1.urls)),
]
