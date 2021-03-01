from django.urls import path
from .views import (
    AdvertisementCreateView, AdvertisementUpdateView, AdvertisementDeleteView, AdvertisementDetailView
    )


app_name = 'advertisement'

urlpatterns = [
    path('create/', AdvertisementCreateView.as_view(), name='advertisement_create'),
    path('<int:pk>/update/', AdvertisementUpdateView.as_view(), name='advertisement_update'),
    path('<int:pk>/delete/', AdvertisementDeleteView.as_view(), name='advertisement_delete'),
    path('<int:pk>/', AdvertisementDetailView.as_view(), name='advertisement_detail'),
]