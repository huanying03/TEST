
# win 7,Python 2.7, Django 1.11 -> webSite

## Prepare
- install Python 2.7, setenv PATH
- install Django 1.11, setenv PATH

## Begin

[ under GitBash ]

- $ django-admin startproject mysite
- $ cd mysite
- $ python manage.py runserver

## manage Database

- $ python manage.py makemigrations
- $ python manage.py migrate
- $ python manage.py syncdb
- $ python manage.py createsuperuser

## Create app

- $ python manage.py startapp blog
- $ vi mysite/settings.py 

INSTALLED_APPS:

  'blog',
  
## Create data model

- $ vi mysite/blog/models.py

for example:

from django.contrib import admin

class BlogPost(models.Model):

  title = Models.CharField(max_length = 50)
  
  content = models.textField()
  
  timestamp = models.DateTimeField()
  
class BlogPostAdmin(admin.ModelAdmin):

  list_display = ('title','content','timestamp')
  
admin.site.register(BlogPost,BlotPostAdmin)

## Create response function

- $ vi blog/views.py

for example:

from django.template import loader

from django.http import HttpResponse,HttpResponseRedirect,JsonResponse,FileResponse

from models import Blog,BlogPost

def archive(request):

  posts = BlogPost.objects.all()
  
  t = loader.get_template('archive.html')
  
  c = {'posts':posts}
  
  return HttpResponse(t.render(c))
  
## Config URL with response function

- $ vi mysite/urls.py

url(r'^$',views,showBlogList),

url(r'^blog/(\d+)$',views.showBlog),

url(r'^blog/',views.archive)

## Create html templates

- $ vi blog/templates/base.html
- $ vi blog/templates/archive.html
- $ vi blog/templates/blog.html
- $ vi blog/templates/blog-list.html
  
