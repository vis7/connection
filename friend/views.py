from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Friend
from user.models import User

# Create your views here.
# detail view of user can be used

class FriendListView(ListView):
    model = Friend
    template_name = 'friend/friend_list.html'

class FriendRequestListView(ListView):
    model = Friend
    template_name = 'friend/friend_request_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['friend_request_list'] = Friend.objects.filter(fr_send_to=self.request.user)
        return context

# class FriendListView(ListView):
#     model = Friend
#     template_name = 'friend/friend_list.html'

def send_friend_request(request):
    # fr_send_by = request.POST.get('fr_send_by', None)
    fr_send_to = request.POST.get('fr_send_to', None)
    # fr_send_by_user = Friend.objects.get(pk=int(fr_send_by))
    fr_send_to_user = User.objects.get(pk=fr_send_to)
    temp = Friend(fr_send_by=request.user, fr_send_to=fr_send_to_user)
    temp.save()
    return redirect('user:user_detail', pk=fr_send_to)

def process_friend_request(request):
    submit_value = request.POST.get('submit_value', False)
    fr_id = request.POST.get('fr_id', None)
    if submit_value == "Accept":
        login_user = request.user
        fr_send_by = request.POST.get('fr_send_by', None)
        fr_send_by_user = User.objects.get(username=fr_send_by)
        # print(fr_send_by)
        # print(login_user)
        login_user.friends.add(fr_send_by_user.user_id)
    fr = Friend.objects.get(id=fr_id)
    # print(fr.id)
    fr.delete()
    # change this to redirect frined request view

    context = {
        'submit_value': submit_value,
    }
    # return render(request, "friend/process_friend_request.html", context=context)
    return redirect('friend:friend_list')

