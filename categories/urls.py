from django.urls import path
from . import views

urlpatterns = [
    path('', views.category, name='catagory'),
    path('categories', views.add_category, name='add_category'),
]
