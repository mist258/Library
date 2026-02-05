from django.db import models

from apps.author.models import AuthorModel

from core.models import BaseModel


class BookModel(BaseModel):
    class Meta:
        db_table = 'books'

    title = models.CharField()
    description = models.TextField()
    publish_date = models.DateField()
    author = models.ForeignKey(AuthorModel,
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True,
                               related_name='author')

    def __str__(self):
        return (f'Book title: {self.title},'
                f'description: {self.description},'
                f'publish_date: {self.publish_date}')