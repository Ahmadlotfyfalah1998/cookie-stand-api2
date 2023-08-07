from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    template_name = "Book/Book_list.html"
    model = Book
    context_object_name = "Book"


class BookDetailView(LoginRequiredMixin, DetailView):
    template_name = "Book/Book_detail.html"
    model = Book


class BookUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "Book/Book_update.html"
    model = Book
    fields = "__all__"


class BookCreateView(LoginRequiredMixin, CreateView):
    template_name = "Book/Book_create.html"
    model = Book
    fields = ["name", "rating", "reviewer"] # "__all__" for all of them


class BookDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "Book/Book_delete.html"
    model = Book
    success_url = reverse_lazy("Book_list")
