from django.test import TestCase

from book.fixtures import GET_BOOK_BY_ID_OBJECT_RETURNED

import requests


class BookTestCase(TestCase):
    def setUp(self) -> None:
        self.url_by_search_term_gutendex = "https://gutendex.com/books?search=dickens%20great"
        self.url_by_id_gutendex = "https://gutendex.com/books/1400"
        self.url_by_search_term_localhost = "http://localhost:8000/books?search_term=dickens%20great"
        self.url_by_id_localhost = "http://localhost:8000/books/1400"
        self.url_post_localhost = "http://localhost:8000/books"

    def test_get_books_from_search_term(self):
        request_to_gutendex = requests.get(self.url_by_search_term_gutendex)
        request_to_localhost = requests.get(self.url_by_search_term_localhost)
        request_external = request_to_gutendex.json().get('results')
        request_local = request_to_localhost.json().get('books')
        self.assertEqual(request_external[0]['authors'], request_local[0]['authors'])
        self.assertEqual(request_external[0]['id'], request_local[0]['id'])
        self.assertEqual(request_external[0]['title'], request_local[0]['title'])
        self.assertEqual(request_external[0]['languages'], request_local[0]['languages'])
        self.assertEqual(request_external[0]['download_count'], request_local[0]['download_count'])

    def test_get_books_from_id(self):
        requests.post(self.url_post_localhost, {
            "book_id": 1400,
            "rating": 5.0,
            "review": "AWESOME BOOK!"
        })
        requests.post(self.url_post_localhost, {
            "book_id": 1400,
            "rating": 1.0,
            "review": "not good at all!"
        })
        request_to_localhost = requests.get(self.url_by_id_localhost)
        request_local = request_to_localhost.json()
        self.assertEqual(request_local['authors'], GET_BOOK_BY_ID_OBJECT_RETURNED['authors'])
        self.assertEqual(request_local['rating'], GET_BOOK_BY_ID_OBJECT_RETURNED['rating'])
