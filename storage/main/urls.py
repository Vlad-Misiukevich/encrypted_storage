from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('note/<int:id>', views.note_page, name='notes')
]
