from django.shortcuts import render, redirect
from .models import Category, Note, Content
from .forms import CategoryForm, NoteForm, ContentForm
import base64


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


def content_page(request, id):
    if request.method == 'POST':
        content_form = ContentForm(request.POST)
        if content_form.is_valid():
            coded_text = content_form.cleaned_data['note_text']
            password = content_form.cleaned_data['password']
            note_text = content_form.cleaned_data['note_text']
            title = content_form.cleaned_data['title']
            note_name = content_form.cleaned_data['note_name']
            new_article = Content(note_name=note_name, title=title, note_text=note_text,
                                  coded_text=coded_text, password=password)
            new_article.save()
            return redirect('home')

    content_form = ContentForm()
    article = Content.objects.filter(note_name_id=id)
    context = {'title': 'Articles', 'article': article, 'form': content_form}
    return render(request, 'main/content_page.html', context)


def encode(string):
    encoded_string = base64.b64encode(string.encode("UTF-8")).decode("UTF-8")
    return encoded_string
