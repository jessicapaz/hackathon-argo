from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Book

class HomeView(TemplateView):
    template_name = 'base.html'

class BookListView(TemplateView):
    model = Book
    template_name = 'lista_livros.html'

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context