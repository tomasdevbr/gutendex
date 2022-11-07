from book.views import BookApiView, BookDetailApiView

from django.urls import path


urlpatterns = [
    path('books', BookApiView.as_view()),
    path('books/<int:book_id>', BookDetailApiView.as_view())
]
