from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    ListView
)

from .models import Community
from .forms import CommunityForm

# Create your views here.
class CommunityObjectMixin(object):
    model = Community
    def get_object(self):
        pk = self.kwargs.get("pk")
        obj = None
        if pk is not None:
            obj = get_object_or_404(self.model, pk=pk)
        return obj

class CommunityCreateView(CreateView):
    template_name = 'community/community_create.html'
    form_class = CommunityForm # this works good but overriden because we need both get and post

class CommunityUpdateView(CommunityObjectMixin, UpdateView):
    model = Community
    template_name = 'community/community_update.html'
    form_class = CommunityForm
    # success_url = reverse_lazy('Community:Community-detail', kwargs={"pk": self.pk})

class CommunityDeleteView(CommunityObjectMixin, DeleteView):
    model = Community
    template_name = 'community/community_delete.html'
    success_url = reverse_lazy('home-view') # try to replace this static url

class CommunityDetailView(CommunityObjectMixin, DetailView):
    model = Community
    # form_class = CommunityModelForm
    template_name = 'community/community_detail.html'

class CommunityListView(ListView):
    model = Community
    template_name = 'community/community_list.html'