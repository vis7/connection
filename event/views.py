from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    ListView
)

from .models import Event
from .forms import EventForm

# Create your views here.
class EventObjectMixin(object):
    model = Event
    def get_object(self):
        pk = self.kwargs.get("pk")
        obj = None
        if pk is not None:
            obj = get_object_or_404(self.model, pk=pk)
        return obj

class EventCreateView(CreateView):
    template_name = 'event/event_create.html'
    form_class = EventForm # this works good but overriden because we need both get and post

class EventUpdateView(EventObjectMixin, UpdateView):
    model = Event
    template_name = 'event/event_update.html'
    form_class = EventForm
    # success_url = reverse_lazy('event:event-detail', kwargs={"pk": self.pk})

class EventDeleteView(EventObjectMixin, DeleteView):
    model = Event
    template_name = 'event/event_delete.html'
    success_url = reverse_lazy('home-view') # try to replace this static url

class EventDetailView(EventObjectMixin, DetailView):
    model = Event
    # form_class = EventModelForm
    template_name = 'event/event_detail.html'

class EventListView(ListView):
    model = Event
    template_name = 'event/event_list.html'


