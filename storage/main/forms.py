from django import forms
from .models import Category, Note


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
