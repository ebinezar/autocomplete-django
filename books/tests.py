from django.test import TestCase
from django.urls import reverse

from books.models import Books

class BooksTestCase(TestCase):
	"""
		Test case for books model
	"""
	@classmethod
	def setUpTestData(cls):
		# Create 13 books for pagination tests
		number_of_books = 13

		for book_id in range(number_of_books):
			Books.objects.create(
				title=f'Book {book_id}',
				author=f'Author {book_id}',
			)

	def test_view_url_exists_at_desired_location(self):
		response = self.client.get('/books')
		self.assertEqual(response.status_code, 200)
		   
	def test_view_url_accessible_by_name(self):
		response = self.client.get(reverse('books_list'))
		self.assertEqual(response.status_code, 200)
		
	def test_view_uses_correct_template(self):
		response = self.client.get(reverse('books_list'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'books/books_list.html')
		
	def test_pagination_is_ten(self):
		response = self.client.get(reverse('books_list'))
		self.assertEqual(response.status_code, 200)
		self.assertTrue('is_paginated' in response.context)
		self.assertTrue(response.context['is_paginated'] == True)
		self.assertTrue(len(response.context['books_list']) == 10)

	def test_lists_all_books(self):
		# Get second page and confirm it has (exactly) remaining 3 items
		response = self.client.get(reverse('books_list')+'?page=2')
		self.assertEqual(response.status_code, 200)
		self.assertTrue('is_paginated' in response.context)
		self.assertTrue(response.context['is_paginated'] == True)
		self.assertTrue(len(response.context['books_list']) == 3)

	def test_delete_and_get_book_details(self):
		response = self.client.get(reverse('book_detail', kwargs={'pk':1}))
		self.assertEqual(response.status_code, 200)

		response = self.client.get(reverse('book_delete', kwargs={'pk':1}))

		response = self.client.get(reverse('book_detail', kwargs={'pk':1}))
		self.assertEqual(response.status_code, 404)
		