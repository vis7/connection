from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    ListView
)

from .models import NewsFeed

# Create your views here.
# newsfeed will be generated by function. can't be edited. can be deleted
# no need for detail view

class NewsFeedListView(ListView):
    model = NewsFeed
    template_name = 'newsfeed/newsfeed_list.html'
