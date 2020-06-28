from django.test import TestCase
from django.urls import reverse

from books.models import Books

class BooksTestCase(TestCase):
    """
        Test case for books model
    """
    def setUp(self):
        Books.objects.create(title="book1", author="author1")
        Books.objects.create(title="book2", author="author2")

    def test_search_book(self):
        """test book added"""
        lion = Books.objects.get(title="lion")
        cat = Books.objects.get(title="cat")
        
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')