from django.db.models import Q
from django.views.generic import ListView

from .models import BookModel


class BookListView(ListView):
    model = BookModel
    template_name = "books/books.html"
    context_object_name = "object_list"
    paginate_by = 10

    def get_queryset(self):
        queryset = BookModel.objects.select_related('author').all()
        q = self.request.GET.get('q')
        sort = self.request.GET.get('sort')

        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(author__name__icontains=q)
            )

        if sort == 'asc':
            queryset = queryset.order_by('publish_date')
        elif sort == 'desc':
            queryset = queryset.order_by('-publish_date')

        return queryset


