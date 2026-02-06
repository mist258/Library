from django.db import models


class AuthorModel(models.Model):
    class Meta:
        db_table = 'authors'

    name = models.CharField(db_index=True, max_length=100)
    email = models.EmailField(null=True, blank=True, unique=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return (f'Author name: {self.name}, '
                f'email: {self.email}, '
                f'bio: {self.bio}')
