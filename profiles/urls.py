from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('add-profile', views.add_profile, name='add_profile'),
]
