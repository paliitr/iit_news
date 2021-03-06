from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.

@python_2_unicode_compatible
class NewsArticle(models.Model):
	post_id = models.CharField(max_length=300)
	title = models.CharField(max_length=300)
	pub_date = models.DateTimeField('date published')
	summary = models.CharField(max_length=600)
	img_src = models.CharField(max_length=300,blank=True,null=True)
	url = models.CharField(max_length=300)
	source = models.CharField(max_length=50)

	def __str__(self):
		return self.title