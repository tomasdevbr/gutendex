from urllib.error import HTTPError

import requests

from json import JSONDecodeError


def request_to_gutendex_by_search_term(search_term: str) -> dict:
    try:
        response = requests.get(f'https://gutendex.com/books?search={search_term}')
        response.raise_for_status()
        return response.json()
    except (requests.exceptions.RequestException, JSONDecodeError, HTTPError, Exception) as e:
        raise SystemExit(e)


def request_to_gutendex_by_id(id: int) -> dict:
    try:
        response = requests.get(f'https://gutendex.com/books/{id}')
        response.raise_for_status()
        return response.json()
    except (requests.exceptions.RequestException, JSONDecodeError, HTTPError, Exception) as e:
        raise SystemExit(e)
