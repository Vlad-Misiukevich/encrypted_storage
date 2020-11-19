from django.shortcuts import render, redirect
from .models import Category, Note
from .forms import CategoryForm, NoteForm


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


def note_page(request, id):
    if request.method == 'POST':
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            note_form.save()
            return redirect('home')

    notes = Note.objects.filter(note_id=id)
    note_form = NoteForm()
    context = {'title': 'Notes', 'notes': notes, 'note_forms': note_form}
    return render(request, 'main/note_page.html', context)
