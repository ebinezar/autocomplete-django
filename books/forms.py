from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from books.models import Books


class BooksForm(forms.ModelForm):
	class Meta:
		model = Books
		fields = ('title', 'author')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Save book'))
