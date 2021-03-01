from django.shortcuts import render
from django.views.generic import ListView

from .models import Notification

# Create your views here.
class NotificationListView(ListView):
    model = Notification
    template_name = 'notification/notification_list.html'

