from django.db import models
from django.contrib.admin.models import User

class Post(models.Model):
	user=models.ForeignKey(User)
	title=models.CharField(max_length=200)
	description=models.TextField()
	pub_date=models.DateTimeField("Date Published", auto_now=True, auto_now_add=True)
	publish=models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.title
	
	"""
	class Meta:
		db_table = 'new_table_name'
	"""

class Comment(models.Model):
	user=models.ForeignKey(User)
	post=models.ForeignKey(Post) #Comment.objects.filter(post_id= Post.objects.get(id=post_id))
	title=models.CharField(max_length=200)
	description=models.TextField()
	pub_date=models.DateTimeField("Date Published", auto_now=True, auto_now_add=True)
	publish=models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.title
	

	
	
