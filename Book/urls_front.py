from django.urls import path
from .views_front import (
    BookCreateView,
    BookDeleteView,
    BookDetailView,
    BookListView,
    BookUpdateView,
)

urlpatterns = [
    path("", BookListView.as_view(), name="Book_list"),
    path("<int:pk>/", BookDetailView.as_view(), name="Book_detail"),
    path("create/", BookCreateView.as_view(), name="Book_create"),
    path("<int:pk>/update/", BookUpdateView.as_view(), name="Book_update"),
    path("<int:pk>/delete/", BookDeleteView.as_view(), name="Book_delete"),
]
