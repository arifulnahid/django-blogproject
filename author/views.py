from django.shortcuts import render, redirect
from .forms import AuthorForm
from .models import Author

# Create your views here.


def author(request):
    authors = Author.objects.all()
    return render(request, 'author.html', {'authors': authors})


def add_author(request):
    author_form = AuthorForm()

    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('author')

    return render(request, 'author.html', {'form': author_form})
