from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    ListView
)

from .models import Advertisement
from .forms import AdvertiserForm

# Create your views here.
class AdvertisementObjectMixin(object):
    model = Advertisement
    def get_object(self):
        pk = self.kwargs.get("pk")
        obj = None
        if pk is not None:
            obj = get_object_or_404(self.model, pk=pk)
        return obj

class AdvertisementCreateView(CreateView):
    template_name = 'advertisement/advertisement_create.html'
    form_class = AdvertiserForm # this works good but overriden because we need both get and post

class AdvertisementUpdateView(AdvertisementObjectMixin, UpdateView):
    model = Advertisement
    template_name = 'advertisement/advertisement_update.html'
    form_class = AdvertiserForm
    # success_url = reverse_lazy('user:user-detail', kwargs={"pk": self.pk})

class AdvertisementDeleteView(AdvertisementObjectMixin, DeleteView):
    model = Advertisement
    template_name = 'advertisement/advertisement_delete.html'
    success_url = reverse_lazy('home-view') # try to replace this static url

class AdvertisementDetailView(AdvertisementObjectMixin, DetailView):
    model = Advertisement
    template_name = 'advertisement/advertisement_detail.html'
    # context_object_name = 'advertisement' # thsi is default

