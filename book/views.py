from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from book.serializers import BookListSerializer, ReviewSerializer, BookDetailSerializer
from utils.gutendex import request_to_gutendex_by_search_term, request_to_gutendex_by_id


search_term = openapi.Parameter(
    'search_term',
    openapi.IN_QUERY,
    description="Term used to get book data",
    type=openapi.TYPE_STRING
)


class BookApiView(APIView):

    @swagger_auto_schema(
        responses={200: BookListSerializer(many=True)},
        manual_parameters=[search_term],
        operation_description='Endpoint to return all books that contains the search term'
    )
    def get(self, request):
        search_term = request.query_params.get('search_term')
        data = request_to_gutendex_by_search_term(search_term)
        serializer = BookListSerializer(data['results'], many=True)
        return Response({'books': serializer.data})

    @swagger_auto_schema(
        request_body=ReviewSerializer,
        responses={200: "{'success': 'Review created successfully'}"},
        operation_description='Endpoint to create a review for a specific book'
    )
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'success': 'Review created successfully'})


class BookDetailApiView(APIView):

    @swagger_auto_schema(
        responses={200: BookDetailSerializer()},
        operation_description='Endpoint to get data from a specific book'
    )
    def get(self, request, book_id):
        data = request_to_gutendex_by_id(book_id)
        serializer = BookDetailSerializer(data)
        return Response(serializer.data, status=HTTP_200_OK)
