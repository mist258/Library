from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from apps.books.models import BookModel

from .models import AuthorModel


class AuthorListView(ListView):
    model = AuthorModel
    template_name = "authors/authors.html"
    context_object_name = "object_list"
    paginate_by = 12

    def get_queryset(self):
        return AuthorModel.objects.annotate(books_count=Count('books'))


class AuthorListDetailsView(ListView):
    model = AuthorModel
    template_name = "authors/authors_books.html"
    context_object_name = "object_list"
    paginate_by = 7

    def get_queryset(self):
        author = get_object_or_404(AuthorModel, pk=self.kwargs['pk'])
        return BookModel.objects.filter(author=author).select_related('author')

