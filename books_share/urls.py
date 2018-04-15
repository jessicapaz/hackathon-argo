from django.urls import path
from .views import HomeView, BookListView

urlpatterns = [
    path('', HomeView.as_view()),
    path('lista-livros', BookListView.as_view()),
]
