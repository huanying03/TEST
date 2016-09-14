# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# add an import for admin
from django.contrib import admin

# add a Model for Author
class Author(models.Model):
	name = models.CharField(max_length = 50 )
	age = models.IntegerField()
	def __unicode__(self):
		return self.name
class AuthorAdmin(admin.ModelAdmin):
	list_display=('name','age')
admin.site.register(Author,AuthorAdmin)


# add a Model for Blog 
class Blog(models.Model):
	title = models.CharField(max_length = 50 )
	content = models.TextField()
	counter = models.IntegerField(default = 0)
	putDate = models.DateField(auto_now_add =True)
	author = models.ForeignKey(Author)
	def __unicode__(self):
		return self.title		
class BlogAdmin(admin.ModelAdmin):
	list_display = ('title','content','author')
admin.site.register(Blog,BlogAdmin)

# add a Model for BlogPost
class BlogPost(models.Model):
	title = models.CharField(max_length = 50)
	content = models.TextField()
	timestamp = models.DateTimeField()
	def __unicode__(self):
		return self.title
class BlogPostAdmin(admin.ModelAdmin):
	list_display = ()
admin.site.register(BlogPost,BlogPostAdmin)
