from django.urls import path
from .views import (
    EventCreateView, EventUpdateView, EventDeleteView, EventDetailView, EventListView
    )


app_name = 'event'

urlpatterns = [
    path('create/', EventCreateView.as_view(), name='event_create'),
    path('<int:pk>/update/', EventUpdateView.as_view(), name='event_update'),
    path('<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    path('<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('event_list/', EventListView.as_view(), name='event_list')
]