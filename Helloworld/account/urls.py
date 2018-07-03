from django.conf.urls import url
from . import views

# from blog.views import blog_title, blog_article

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='user_login'),
]
