from django.urls import path, re_path
# from django.conf.urls import url # url() is depreciated over re_path()
from .views import (
    PostCreateView, PostUpdateView, PostDeleteView, PostDetailView, PostListView,
    CommentCreateView, CommentUpdateView, CommentDeleteView, CommentListView, CommentDetailView
    )


app_name = 'post'

urlpatterns = [
    re_path(r'^create/$', PostCreateView.as_view(), name='post_create'),
    # path('<int:pk>/', PostDet ailView.as_view(), name='post_detail'),
    re_path(r'^(?P<pk>[0-9])/update/$', PostUpdateView.as_view(), name='post_update'),
    re_path(r'^(?P<pk>[0-9])/delete/$', PostDeleteView.as_view(), name='post_delete'),
    re_path(r'^(?P<pk>[0-9])/$', PostDetailView.as_view(), name='post_detail'),
    path('post_list/', PostListView.as_view(), name='post_list'),

    # # for comment it will be post/comment
    re_path(r'^(?P<post_id>[0-9])/comment/create/$', CommentCreateView.as_view(), name='comment_create'),
    re_path(r'^comment/(?P<pk>[0-9])/update/$', CommentUpdateView.as_view(), name='comment_update'),
    re_path(r'^comment/(?P<pk>[0-9])/delete/$', CommentDeleteView.as_view(), name='comment_delete'),
    re_path(r'^(?P<post_id>[0-9])/comment/comment_list/$', CommentListView.as_view(), name='comment_list'),
    re_path(r'^comment/(?P<pk>[0-9])/$', CommentDetailView.as_view(), name='comment_detail'),

]

