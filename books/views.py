
from django.views.generic import View
from django.http import JsonResponse

from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from books.models import Books
from books.forms import BooksForm


class BooksListView(ListView):
	"""
		View to display list of books
	"""
	model = Books
	paginate_by = 10  # if pagination is desired
	context_object_name = 'books_list'
	
	def get_queryset(self):
		query = self.request.GET.get('q')
		if query:
			return Books.objects.filter(title=query).order_by('title')
		
		return Books.objects.all().order_by('title')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['q'] = self.request.GET.get('q')
		return context


class BooksDetailView(DetailView):
	"""
		View to display a book details
	"""
	model = Books

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context


class BooksCreateView(CreateView):
	"""
		View to create a book
	"""
	model = Books
	fields = ('title', 'author')
	success_url = reverse_lazy('books_list')


class BooksUpdateView(UpdateView):
	"""
		View to update a book
	"""
	model = Books
	form_class = BooksForm
	success_url = reverse_lazy('books_list')


class BooksDeleteView(View):
	"""
		View to delete a book
	"""
	model = Books

	def get(self, request, pk):
		"""
		Delete object
		params:
		 - pk (int)
		"""
		Books.objects.filter(id=pk).delete()
		return redirect('books_list')
		

class Autocomplete(View):
	"""
		Autocomplete api to search and provide list of books
	"""
	def get(self, request):
		
		query = request.GET.get('q')

		if not query:
			return JsonResponse([], safe=False)

		result = Books.objects.filter(title__icontains=query).order_by('title').values('title')[:10]
		return JsonResponse(list(result), safe=False)
