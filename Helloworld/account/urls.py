from django.conf.urls import url
from . import views

from django.conf import settings

from django.contrib.auth import views as auth_views

# from blog.views import blog_title, blog_article

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^login/$', views.user_login, name='user_login'),  # 自定义的登录
    url(r'^login/$', auth_views.login, name='user_login'),  # django内置登录

]
