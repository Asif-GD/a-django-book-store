from django.db import models
from django_extensions.db.models import TitleSlugDescriptionModel

# Create your models here.
# Book Model
"""
_________________________________________________
| BookList                                      |
-------------------------------------------------
| title                         TEXT            |
| book_isbn_13                  INTEGER (UNIQUE)|
| book_author                   TEXT            |
| book_year_of_publication      INTEGER         |
| book_genre                    TEXT            |
| book_availability             BOOLEAN         |
| book_delete_status            BOOLEAN         |
-------------------------------------------------
"""


class BookList(TitleSlugDescriptionModel,
               models.Model):
    """
    Stores a single book entry for our book store
    """

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ["id"]

    def __str__(self):
        return self.title

    # basic information fields
    title = models.CharField(max_length=300)
    book_isbn_13 = models.IntegerField(unique=True)
    book_author = models.CharField(max_length=100)
    book_year_of_publication = models.IntegerField()
    book_genre = models.CharField(max_length=300)
    book_availability = models.BooleanField(default=True)  # stock checking
    book_delete_status = models.BooleanField(default=False)  # soft deletion
