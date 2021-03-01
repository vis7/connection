from django.urls import path
from .views import (
    NotificationListView
    )


app_name = 'notification'

urlpatterns = [
    path('notification_list/', NotificationListView.as_view(), name='notification_list'),
]