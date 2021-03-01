from django.urls import path, re_path
from .views import (
    UserCreateView, UserUpdateView, UserDeleteView, UserDetailView, UserListView,
    AdvertiserCreateView, AdvertiserUpdateView, AdvertiserDeleteView, AdvertiserDetailView)


app_name = 'user'

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    re_path(r'^(?P<pk>[0-9])+/$', UserDetailView.as_view(), name='user_detail'),
    path('user_list/', UserListView.as_view(), name='user_list'),

    # for advertiser it will be user/advertiser
    path('advertiser/create/', AdvertiserCreateView.as_view(), name='advertiser_create'),
    path('advertiser/<int:pk>/update/', AdvertiserUpdateView.as_view(), name='advertiser_update'),
    path('advertiser/<int:pk>/delete/', AdvertiserDeleteView.as_view(), name='advertiser_delete'),
    path('advertiser/<int:pk>/', AdvertiserDetailView.as_view(), name='advertiser_detail'),

]

