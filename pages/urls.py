# pages/urls.py

from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView # updated

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),      # added
    path('connect/', ContactPageView.as_view(), name='connect'),
    path('',HomePageView.as_view(),name='home')
]