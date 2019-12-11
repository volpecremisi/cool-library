from django.shortcuts import render
from django.views import generic

from .models import Book

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'book_lists'

    def get_queryset(self):
        """
        Return the last ten Books insered or updated in the library
        """
        topTenBooks = Book.objects.all()
        topTenBooks = list(topTenBooks)
        topTenBooks.reverse()
        return topTenBooks[:10]