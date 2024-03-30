from django import template
from blog.models import Post
register = template.Library()

@register.simple_tag(name = 'totalposts')
def function():
    post = Post.objects.filter(status=1).count()
    return post
    
@register.simple_tag(name = 'posts')
def function():
    post = Post.objects.filter(status=1)
    return post

@register.filter
def snippet(value, arg=20):
    return value [:arg] +'...'

@register.inclusion_tag('popularposts.html')
def popularposts():
    posts = Post.objects.filter(status=1).order_by('published_date')
    return {'posts' : posts}