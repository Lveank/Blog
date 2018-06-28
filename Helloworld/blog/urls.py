from django.conf.urls import url
from . import views

# from blog.views import blog_title, blog_article

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.blog_title, name='blog_title'),
    url(r'(?P<article_id>\d)/$', views.blog_article, name='blog_article'),
]
