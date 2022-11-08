from urllib.error import HTTPError

import requests

from json import JSONDecodeError


def request_to_gutendex_by_search_term(search_term: str) -> dict:
    """
    Function to return data from books by a search term
    :param str search_term: Search term used to find books
    :return: A dict with books
    :rtype: dict
    """
    try:
        response = requests.get(f'https://gutendex.com/books?search={search_term}')
        response.raise_for_status()
        return response.json()
    except (requests.exceptions.RequestException, JSONDecodeError, HTTPError, Exception) as e:
        raise SystemExit(e)


def request_to_gutendex_by_id(id: int) -> dict:
    """
    Function to return data from a specific book
    :param int id: Book id to use in gutendex search
    :return: A dict with specific book
    :rtype: dict
    """
    try:
        response = requests.get(f'https://gutendex.com/books/{id}')
        print(response)
        response.raise_for_status()
        return response.json()
    except (requests.exceptions.RequestException, JSONDecodeError, HTTPError, Exception) as e:
        raise SystemExit(e)
