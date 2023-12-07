from django.db import models

# Create your models here.
# Book Model
"""
_________________________________________________
| BookList                                      |
-------------------------------------------------
| book_title                    TEXT            |
| book_isbn                     INTEGER         |
| book_author                   TEXT            |
| book_year_of_publication      INTEGER         |
| book_genre                    TEXT            |
| book_availability             INTEGER (1/0)   |
-------------------------------------------------
"""


class BookList(models.Model):
    # basic information
    book_title = models.CharField(max_length=300)
    book_isbn = models.IntegerField()
    book_author = models.CharField(max_length=100)
    book_year_of_publication = models.IntegerField()
    book_genre = models.CharField(max_length=300)
    # stock checking
    book_availability = models.BooleanField(default=True)
    # soft deletion
    book_delete_status = models.BooleanField(default=False)

    def __str__(self):
        return self.book_title
