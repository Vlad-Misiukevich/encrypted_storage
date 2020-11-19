from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('note/<int:id>', views.note_page, name='notes'),
    path('note/content/<int:id>', views.content_page, name='content')
]
