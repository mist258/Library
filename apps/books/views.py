from django.views.generic import ListView

from .models import BookModel


class BookListView(ListView):
    model = BookModel
    template_name = "books/books.html"
    context_object_name = "object_list"
    paginate_by = 10

    def get_queryset(self):
        return BookModel.objects.select_related('author').all()



