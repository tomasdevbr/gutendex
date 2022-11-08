from decimal import Decimal

from django.db import models
from django.db.models import Avg


class ReviewBook(models.Model):
    """
    Class to store the reviews from a specific book
    :cvar int book_id:
    :cvar Decimal rating:
    :cvar str review:
    :cvar Manager objects
    """
    book_id = models.IntegerField()
    rating = models.DecimalField(decimal_places=1, max_digits=2)
    review = models.TextField()

    objects = models.Manager()

    def __str__(self):
        return f'Review {self.pk} from book {self.book_id} with rating {self.rating}'

    @classmethod
    def get_reviews_from_book(cls, book_id: int) -> list:
        """
        Class method to get reviews from a specific book
        :param int book_id:
        :return: All reviews from a specific book
        :rtype: list
        """
        return [book.review for book in cls.objects.filter(book_id=book_id)]

    @classmethod
    def get_average_ratings_from_book(cls, book_id: int) -> Decimal:
        """
        Class method to get the average rating from a specific book
        :param int book_id:
        :return: Average rating from a specific book
        :rtype: Decimal
        """
        return cls.objects.filter(book_id=book_id).aggregate(Avg('rating')).get('rating__avg', 0)
