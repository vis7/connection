from django.urls import path
from .views import (
    NewsFeedListView
    )


app_name = 'newsfeed'

urlpatterns = [
    path('newsfeed_list/', NewsFeedListView.as_view(), name='newsfeed_list'),
]