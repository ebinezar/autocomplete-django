from django.db import models

class Books(models.Model):
	"""
		Books model along with required fields
	"""
	title = models.CharField(max_length=200, db_index=True)
	author = models.CharField(max_length=200)
	