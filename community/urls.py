from django.urls import path
from .views import (
    CommunityCreateView, CommunityUpdateView, CommunityDeleteView, CommunityDetailView,
    CommunityListView,)


app_name = 'community'

urlpatterns = [
    path('create/', CommunityCreateView.as_view(), name='community_create'),
    path('<int:pk>/update/', CommunityUpdateView.as_view(), name='community_update'),
    path('<int:pk>/delete/', CommunityDeleteView.as_view(), name='community_delete'),
    path('<int:pk>/', CommunityDetailView.as_view(), name='community_detail'),
    path('community_list/', CommunityListView.as_view(), name='community_list'),

]

