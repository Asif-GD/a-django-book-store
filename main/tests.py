from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from .models import BookList


# Create your tests here.

class AddBookTestCase(APITestCase):
    """
    Test suite for add_book
    """

    def setUp(self):
        self.client = APIClient()
        self.data = {
            "data": {
                "type": "add_book",
                "attributes": {
                    "book_title": "Atomic Habits",
                    "book_isbn_13": 9781847941831,
                    "book_author": "James Clear",
                    "book_year_of_publication": 2018,
                    "book_genre": "self-help",
                    "book_availability": True,
                    "book_delete_status": False
                }
            }
        }
        self.url = "/add_book/"

    def test_create_book(self):
        """
        test adding book to database
        """
        data = self.data
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(BookList.objects.count(), 1)
        self.assertEqual(BookList.objects.get().book_title, "Atomic Habits")

    def test_add_book_without_book_title_field(self):
        """
        test add_book when book_title field is not in data
        """
        data = self.data
        data["data"]["attributes"].pop("book_title")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_book_when_book_title_field_is_empty(self):
        """
        test add_book when book_title field is blank
        """
        data = self.data
        data["data"]["attributes"]["book_title"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_book_without_book_isbn_13_field(self):
        """
        test if the book_isbn_13 field is blank
        """
        data = self.data
        data["data"]["attributes"].pop("book_isbn_13")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_book_when_book_isbn_13_field_is_empty(self):
        """
        test if the book_isbn_13 field is empty or not int
        """
        data = self.data
        data["data"]["attributes"]["book_isbn_13"] = None
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_book_without_book_author_field(self):
        """
        test add_book when book_author field is not in data
        """
        data = self.data
        data["data"]["attributes"].pop("book_author")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_book_when_book_author_field_is_empty(self):
        """
        test add_book when book_author field is blank
        """
        data = self.data
        data["data"]["attributes"]["book_author"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_book_without_book_year_of_publication_field(self):
        """
        test if the book_year_of_publication field is blank
        """
        data = self.data
        data["data"]["attributes"].pop("book_year_of_publication")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_book_when_book_year_of_publication_field_is_empty(self):
        """
        test if the book_year_of_publication field is empty or not int
        """
        data = self.data
        data["data"]["attributes"]["book_year_of_publication"] = None
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_book_without_book_genre_field(self):
        """
        test add_book when book_genre field is not in data
        """
        data = self.data
        data["data"]["attributes"].pop("book_genre")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_book_when_book_genre_field_is_empty(self):
        """
        test add_book when book_genre field is blank
        """
        data = self.data
        data["data"]["attributes"]["book_genre"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_book_when_book_availability_field_is_not_boolean(self):
        """
        test if the book_availability field is not boolean
        """
        data = self.data
        data["data"]["attributes"]["book_availability"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_book_when_book_delete_status_field_is_not_boolean(self):
        """
        test if the book_delete_status field is not boolean
        """
        data = self.data
        data["data"]["attributes"]["book_delete_status"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
