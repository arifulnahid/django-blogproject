from django.urls import path
from . import views

urlpatterns = [
    path('', views.post, name='post'),
    path('add-post', views.add_post, name='add_post'),
    path('edit-post/<int:id>', views.edit_post, name='edit_post'),
    path('delete-post/<int:id>', views.delete_post, name='delete_post'),
]
