from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Book
from .permissions import IsOwnerOrReadOnly
from .serializers import Bookerializer


class BookList(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookerializer


class BookDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = Bookerializer
