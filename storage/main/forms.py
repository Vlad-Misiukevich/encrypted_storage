from django import forms
from .models import Category, Note, Content


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']
        widgets = {
            'category': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Введите категорию'})
        }


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['note_name', 'note']
        widgets = {
            'note_name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Введите заметку'}),
            'note': forms.Select(attrs={'class': 'form-control'})
        }


class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['note_name', 'title', 'note_text', 'password']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'note_text': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Введите текст'}),
            'password': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Введите пароль'}),
            'note_name': forms.Select(attrs={'class': 'form-control'})
        }
