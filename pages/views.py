from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# this app display connection specific pages.
# Create your views here.
@login_required
def home_view(request, *args, **kwargs):
    c_user = request.user
    # msg = ''
    # if request.user.is_authenticated:
    #     msg = 'yes'
    # else:
    #     msg = 'no'

# if request.user.is_authenticated():
#          user = request.user

    context = {
        'c_user': c_user,
        # 'msg': msg
    }
    return render(request, "home.html", context)

def logout_home_view(request, *args, **kwargs):
    context = {}
    return render(request, "logout_home.html", context)

def guest_view(request, *args, **kwargs):
    context = {}
    return render(request, "guest_home.html", context)