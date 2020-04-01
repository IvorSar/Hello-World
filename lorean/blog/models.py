from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from transliterate import translit

class Post(models.Model):
	STATUS_CHOICES = (
		('draft' , 'Draft'), #Проект
		('published' , 'Published'), # Опубликован

	)
	title = models.CharField(max_length = 250)
	slug = models.SlugField(max_length = 250 , unique_for_date = 'publish')
	author = models.ForeignKey(User , on_delete = models.CASCADE , related_name = 'blog_posts')
	body = models.TextField()
	publish = models.DateTimeField(default = timezone.now)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	status = models.CharField(max_length = 10 , choices = STATUS_CHOICES , default = 'draft')

	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title

class Video(models.Model):
	title = models.CharField(max_length = 250)
	slug = models.SlugField(max_length = 250 )
	publish = models.DateTimeField(default = timezone.now)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	video = models.FileField(upload_to="upload_location",blank=True,null=True)

	def __str__(self):
		return self.title


