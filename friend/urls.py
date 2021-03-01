from django.urls import path, re_path
from .views import (
    FriendListView,
    FriendRequestListView,
    send_friend_request,
    process_friend_request
    )


app_name = 'friend'

urlpatterns = [
    path('friend_list/', FriendListView.as_view(), name='friend_list'),
    re_path(r'^send_friend_request/$', send_friend_request, name='send_friend_request'),
    path('friend_request_list/', FriendRequestListView.as_view(), name='friend_request_list'),
    path('process_friend_request/', process_friend_request, name='process_friend_request'),
]