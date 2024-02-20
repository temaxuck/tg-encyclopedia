import abc
import requests

from typing import Any, Tuple, List
from urllib.parse import quote_plus


class APIService(abc.ABC):
    """
    Abstract class for api services.

    Api services should be initialized with api_url parameter
    """

    api_url = None

    @abc.abstractmethod
    def __init__(self, api_url: str) -> None:
        """
        Initialize api service.

        Must have api_url attribute

        Args:
            api_url (str): url for API services
        """
        raise NotImplemented


class OENPService(APIService):
    def __init__(self, api_url: str) -> None:
        """Initialize OENPService

        Args:
            api_url (str): url to the Online Encyclopedia of Number Pyramids api endpoint
        """
        self.api_url = api_url

    def get_pyramid_by_sequence_number(self, sequence_number: int) -> dict:
        """Get Pyramid (dict object) by pyramid sequence number

        Args:
            sequence_number (int): pyramid's sequence number according to Online Encyclopedia of Number Pyramids https://oenp.tusur.ru/

        Returns:
            dict: Pyramid object
        """
        response = requests.get(f"{self.api_url}/pyramid/{sequence_number}").json()

        return response

    def search_pyramid_by_generating_function(self, query: str) -> dict:
        response = requests.get(
            f"{self.api_url}/search?search_type=0&search_query={quote_plus(query)}"
        ).json()

        return response

    def search_pyramid_by_explicit_formula(self, query: str) -> dict:
        response = requests.get(
            f"{self.api_url}/search?search_type=0&search_query={quote_plus(query)}"
        ).json()

        return response

    def search_pyramid_by_data(self, query: str) -> dict:
        response = requests.get(
            f"{self.api_url}/search?search_type=1&search_query={quote_plus(query)}"
        ).json()

        return response


class OEISService(APIService):
    def __init__(self, api_url: str) -> None:
        """
        Initialize OEISService

        Args:
            api_url (str): url to the On-Line Encyclopedia of Integer Sequences api endpoint
        """
        self.api_url = api_url

    def get_sequence_by_data(self, data: List[Any]) -> Tuple[dict, str]:
        """Get Pyramid (dict object) by pyramid sequence number

        Args:
            data (List[int]): pyramid's data according to Online Encyclopedia of Number Pyramids https://oenp.tusur.ru/

        Returns:
            Tuple(dict, str): pair of values json-response and url (not api) to the sequence
        """

        api_url = f"{self.api_url}/search?fmt=json&q={quote_plus(str(data))}"
        response = requests.get(api_url).json()
        url = f"{self.api_url}/search?q={quote_plus(str(data))}"

        return (response, url)
