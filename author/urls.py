from django.urls import path
from . import views

urlpatterns = [
    path('', views.author, name='author'),
    path('add-author', views.add_author, name='add_author')
]
