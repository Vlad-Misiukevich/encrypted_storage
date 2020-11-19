from django.shortcuts import render, redirect
from .models import Category
from .forms import CategoryForm


def index(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('home')

    categories = Category.objects.all()
    form = CategoryForm()
    context = {'title': 'Category', 'category': categories, 'form': form}
    return render(request, 'main/index.html', context)
