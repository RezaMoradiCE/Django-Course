from django.urls import path
from blog.views import *
app_name = 'blog'
urlpatterns = [
    path('', blog_home , name= "home"), 
    path('single', blog_single, name= "single"),
]
