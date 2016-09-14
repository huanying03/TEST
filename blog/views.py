# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hello(request):
	return HttpResponse('<html>Hello World</html>')
	
def showBlog(request,blogId):
	t = loader.get_template('blog.html')
	blog = Blog.objects.get(id=blogId)
	context = {'blog':blog}
	html = t.render(context)
	return HttpResponse(html)
	
def showBlogList(request):
	t = loader.get_template('blog-list.html')
	blogs = Blog.objects.all()
	context = {'blogs':blogs}
	html = t.render(context)
	return HttpResponse(html)
	
def archive(request):
	posts = BlogPost.objects.all()
	t = loader.get_template('archive.html')
	c = {'posts':posts}
	return HttpResponse(t.render(c))
	