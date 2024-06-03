from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

# Create your views here.


def post(request):
    posts = Post.objects.all()
    return render(request, 'post.html', {'posts': posts})


def add_post(request):
    post_form = PostForm()
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('post')
    return render(request, 'post.html', {'form': post_form})


def edit_post(request, id):
    post = Post.objects.get(pk=id)
    post_form = PostForm(instance=post)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('home')
    return render(request, 'post.html', {'form': post_form})


def delete_post(request, id):
    try:
        post = Post.objects.get(pk=id)
        post.delete()
        return redirect('home')
    except:
        return redirect('home')
