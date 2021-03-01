"""connection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from pages.views import home_view, guest_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # includes
    path('user/', include('user.urls')),
    path('advertisement/', include('advertisement.urls')),
    path('community/', include('community.urls')),
    path('newsfeed/', include('newsfeed.urls')),
    path('notification/', include('notification.urls')),
    path('event/', include('event.urls')),
    path('post/', include('post.urls')),
    # path('search/', include('search.urls')),
    # path('user_setting/', include('user_setting.urls')),
    path('friend/', include('friend.urls')),
    path('core/', include('core.urls')),

    # path('', include('pages.urls')), # think about this
    # connection specific view url mapping
    path('', home_view, name='home_view'),
    path('guest/', guest_view, name='guest_view'),

    # path('', include('pages.urls')),
    # urls for user authentication
    path('accounts/', include('django.contrib.auth.urls')),
    # above single line will give bellow 8 urls
        # accounts/ login/ [name='login']
        # accounts/ logout/ [name='logout']
        # accounts/ password_change/ [name='password_change']
        # accounts/ password_change/done/ [name='password_change_done']
        # accounts/ password_reset/ [name='password_reset']
        # accounts/ password_reset/done/ [name='password_reset_done']
        # accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
        # accounts/ reset/done/ [name='password_reset_complete']
]


if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
