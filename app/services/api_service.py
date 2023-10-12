import requests
import json


class OENPService:
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
