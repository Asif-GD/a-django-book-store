from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from main.models import BookList


# Create your tests here.

class BookListTestCase(APITestCase):
    """
    Test suite for BookListViewSet
    """

    def setUp(self):
        BookList.objects.create(title="Harry Potter and the Philosopher\'s Stone", book_isbn_13=9781408855652,
                                book_author="J.K. Rowling", book_year_of_publication=2014, book_genre="fantasy")
        BookList.objects.create(title="Harry Potter and the Chamber of Secrets", book_isbn_13=9781408855669,
                                book_author="J.K. Rowling", book_year_of_publication=2014, book_genre="fantasy")
        BookList.objects.create(title="Harry Potter and the Prisoner of Azkaban", book_isbn_13=9781408855676,
                                book_author="J.K. Rowling", book_year_of_publication=2014, book_genre="fantasy")
        BookList.objects.create(title="Harry Potter and the Goblet of Fire", book_isbn_13=9781408855683,
                                book_author="J.K. Rowling", book_year_of_publication=2014, book_genre="fantasy")
        self.books = BookList.objects.all()
        self.user = User.objects.create_user(
            username='testuser1',
            password='this_is_a_test',
            email='testuser1@test.com'
        )

        # app uses token authentication
        self.token = Token.objects.get(user=self.user)
        self.client = APIClient()
        # we pass the token in all calls to the API
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.data = {
            "data": {
                "type": "BookList",
                "attributes": {
                    "title": "Atomic Habits",
                    "book_isbn_13": 9781847941831,
                    "book_author": "James Clear",
                    "book_year_of_publication": 2018,
                    "book_genre": "self-help",
                    "book_availability": True,
                    "book_delete_status": False
                }
            }
        }

        self.url = "/book/"

    def test_get_all_books(self):
        """
        test BookListViewSet list method
        """
        self.assertEqual(self.books.count(), 4)
        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_book(self):
        """
        test BookListViewSet retrieve method
        :return: Ok
        """
        for book in self.books:
            response = self.client.get(path=self.url + f"{book.id}/")
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        """
        test BookListViewSet create method
        """
        response = self.client.post(path=self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_without_title_field(self):
        """
        test BookListViewSet create method when title field is not in data
        """
        self.data["data"]["attributes"].pop("title")
        response = self.client.post(path=self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_book_when_title_field_is_empty(self):
        """
        test BookListViewSet create method when title field is blank
        """
        self.data["data"]["attributes"]["title"] = ""
        response = self.client.post(path=self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_book_without_book_isbn_13_field(self):
        """
        test BookListViewSet create method when the book_isbn_13 field is blank
        """
        self.data["data"]["attributes"].pop("book_isbn_13")
        response = self.client.post(path=self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_book_when_book_isbn_13_field_is_empty(self):
        """
        test BookListViewSet create method when the book_isbn_13 field is empty or not int
        """
        self.data["data"]["attributes"]["book_isbn_13"] = None
        response = self.client.post(path=self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_book_without_book_author_field(self):
        """
        test BookListViewSet create method when book_author field is not in data
        """
        self.data["data"]["attributes"].pop("book_author")
        response = self.client.post(path=self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_book_when_book_author_field_is_empty(self):
        """
        test BookListViewSet create method when book_author field is blank
        """
        self.data["data"]["attributes"]["book_author"] = ""
        response = self.client.post(path=self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_book_without_book_year_of_publication_field(self):
        """
        test BookListViewSet create method when the book_year_of_publication field is blank
        """
        self.data["data"]["attributes"].pop("book_year_of_publication")
        response = self.client.post(path=self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_book_when_book_year_of_publication_field_is_empty(self):
        """
        test BookListViewSet create method when the book_year_of_publication field is empty or not int
        """
        self.data["data"]["attributes"]["book_year_of_publication"] = None
        response = self.client.post(path=self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_book_without_book_genre_field(self):
        """
        test BookListViewSet create method when book_genre field is not in data
        """
        self.data["data"]["attributes"].pop("book_genre")
        response = self.client.post(path=self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_book_when_book_genre_field_is_empty(self):
        """
        test BookListViewSet create method when book_genre field is blank
        """
        self.data["data"]["attributes"]["book_genre"] = ""
        response = self.client.post(path=self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_book_when_book_availability_field_is_not_boolean(self):
        """
        test BookListViewSet create method when the book_availability field is not boolean
        """
        self.data["data"]["attributes"]["book_availability"] = ""
        response = self.client.post(path=self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_book_when_book_delete_status_field_is_not_boolean(self):
        """
        test BookListViewSet create method when the book_delete_status field is not boolean
        """
        self.data["data"]["attributes"]["book_delete_status"] = ""
        response = self.client.post(path=self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_soft_delete_book(self):
    #     """
    #     test BookListViewSet delete method
    #     :return:
    #     """
    #     book = self.data["data"]["attributes"]
    #     self.assertEqual(book["book_delete_status"], False)
    #     book["book_delete_status"] = True
    #     response = self.client.patch(path=self.url + f"{self.books[0].id}/", data=self.data)
    #     self.assertEqual(book["book_delete_status"], True)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
