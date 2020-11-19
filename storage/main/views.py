from django.shortcuts import render


def index(request):
    context = {'title': 'Category'}
    return render(request, 'main/index.html', context)
