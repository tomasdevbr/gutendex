from decimal import Decimal

from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from book.models import ReviewBook


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewBook
        fields = ('book_id', 'rating', 'review')

    def validate_book_id(self, value: int) -> int | ValidationError:
        if value or type(value) == int:
            return value
        raise serializers.ValidationError('book_id should be an integer.')

    def validate_rating(self, value: Decimal) -> Decimal | ValidationError:
        if value or type(value) == Decimal:
            return value
        raise serializers.ValidationError('rating should be a decimal number.')

    def validate_review(self, value: str) -> str | ValidationError:
        if value or type(value) == str:
            return value
        raise serializers.ValidationError('review should be a string.')


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

    @swagger_serializer_method(serializer_or_field=serializers.DecimalField)
    def get_rating(self, obj: dict) -> Decimal:
        return round(ReviewBook.get_average_ratings_from_book(obj.get('id')), 1)

    @swagger_serializer_method(serializer_or_field=serializers.ListField)
    def get_reviews(self, obj: dict) -> list:
        return ReviewBook.get_reviews_from_book(obj.get('id'))
