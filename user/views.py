from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    ListView
)

from .forms import UserModelForm, UserProfileModelForm, AdvertiserModelForm
from .models import User, Advertiser
from friend.models import Friend

# Create your views here.
# User Views
class UserObjectMixin(object):
    model = User
    def get_object(self):
        pk = self.kwargs.get("pk")
        obj = None
        if pk is not None:
            obj = get_object_or_404(self.model, pk=pk)
        return obj

class UserCreateView(CreateView):
    template_name = 'user/user_create.html'
    model = User
    form_class = UserModelForm # this works good but overriden because we need both get and post

class UserUpdateView(UserObjectMixin, UpdateView):
    model = User
    template_name = 'user/user_update.html'
    form_class = UserProfileModelForm
    # success_url = reverse_lazy('user:user-detail', kwargs={"pk": self.pk})

class UserDeleteView(UserObjectMixin, DeleteView):
    model = User
    template_name = 'user/user_delete.html'
    success_url = reverse_lazy('home-view') # try to replace this static url

class UserDetailView(UserObjectMixin, DetailView):
    model = User
    template_name = 'user/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_user_id = int(self.kwargs['pk']) #self.request.GET.get('user_id', None)
        logged_user_id = self.request.user.user_id
        if page_user_id == int(logged_user_id): # this seems necessory may be because one thing is returning obj
            is_same_user_as_logged_in = True
        else:
            is_same_user_as_logged_in = False
        # bellow method check is friend
        self.is_friend = False
        friends = self.request.user.friends.all()
        for i in friends:
            if i.user_id == page_user_id:
                    # print('friend')
                    self.is_friend = True
                    break
        # check is friend request send
        try:
            Friend.objects.get(fr_send_by=logged_user_id, fr_send_to=page_user_id)
            context['is_friend_request_send'] = True
        except Friend.DoesNotExist:
            context['is_friend_request_send'] = False
        # if temp != None
        # context['is_friend_request_send'] = False
        context['is_friend'] = self.is_friend
        context['is_same_user_as_logged_in'] = is_same_user_as_logged_in
        context['page_user_id'] = page_user_id
        context['logged_user_id'] = logged_user_id
        return context

class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'

# Advertiser Views
class AdvertiserObjectMixin(object):
    model = Advertiser
    def get_object(self):
        pk = self.kwargs.get("pk")
        obj = None
        if pk is not None:
            obj = get_object_or_404(self.model, pk=pk)
        return obj

class AdvertiserCreateView(CreateView):
    template_name = 'user/advertiser_create.html'
    form_class = AdvertiserModelForm

class AdvertiserUpdateView(AdvertiserObjectMixin, UpdateView):
    model = Advertiser
    template_name = 'user/advertiser_update.html'
    form_class = AdvertiserModelForm

class AdvertiserDeleteView(AdvertiserObjectMixin, DeleteView):
    model = Advertiser
    template_name = 'user/advertiser_delete.html'
    success_url = reverse_lazy('home-view')

class AdvertiserDetailView(AdvertiserObjectMixin, DetailView):
    model = Advertiser
    template_name = 'user/advertiser_detail.html'

class AdvertiserListView(ListView):
    model = Advertiser
    template_name = 'user/advertiser_list.html'


