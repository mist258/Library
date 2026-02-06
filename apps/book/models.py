import datetime

from django.core import validators
from django.db import models

from apps.author.models import AuthorModel

from core.models import BaseModel


class BookModel(BaseModel):
    class Meta:
        db_table = 'books'

    title = models.CharField(validators=[
        validators.MinLengthValidator(2),
        validators.MaxLengthValidator(50)
    ])
    description = models.TextField()
    publish_date = models.DateField(validators=[
        validators.MinValueValidator(datetime.date(1900, 1, 1)),
        validators.MaxValueValidator(datetime.date.today())
    ])
    author = models.ForeignKey(AuthorModel,
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True,
                               related_name='books')

    def __str__(self):
        return (f'Book title: {self.title},'
                f'description: {self.description},'
                f'publish_date: {self.publish_date}')