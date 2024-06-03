from django.shortcuts import render, HttpResponse
from posts.models import Post


def home(reuqest):
    posts = Post.objects.all()
    return render(reuqest, 'home.html', {'posts': posts})
