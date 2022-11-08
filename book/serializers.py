from decimal import Decimal

from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from book.models import ReviewBook


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewBook
        fields = ('book_id', 'rating', 'review')


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField()
    birth_year = serializers.IntegerField()
    death_year = serializers.IntegerField()


class BookListSerializer(serializers.Serializer):
    authors = AuthorSerializer(many=True)
    id = serializers.IntegerField()
    title = serializers.CharField()
    languages = serializers.ListField()
    download_count = serializers.IntegerField()


class BookDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    authors = AuthorSerializer(many=True)
    languages = serializers.ListField()
    download_count = serializers.IntegerField()
    rating = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    def get_rating(self, obj: dict) -> Decimal:
        if ReviewBook.objects.filter(book_id=obj.get('id')).exists():
            return Decimal(round(ReviewBook.get_average_ratings_from_book(obj.get('id')), 1))
        return Decimal(0)

    def get_reviews(self, obj: dict) -> list:
        if ReviewBook.objects.filter(book_id=obj.get('id')).exists():
            return ReviewBook.get_reviews_from_book(obj.get('id'))
        return []
