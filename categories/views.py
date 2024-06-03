from django.shortcuts import render, redirect
from .forms import CategoryForm
from .models import Category

# Create your views here.


def category(reuqest):
    categories = Category.objects.all()
    return render(reuqest, 'category.html', {'categories': categories})


def add_category(request):
    category_form = CategoryForm()
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('catagory')

    return render(request, 'category.html', {'form': category_form})
