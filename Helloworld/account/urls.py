from django.conf.urls import url
from . import views

from django.conf import settings

from django.contrib.auth import views as auth_views  # 为了使用内置的登陆方法，导入了Django内置视图文件

# from blog.views import blog_title, blog_article

urlpatterns = [
    # url(r'^$', views.index, name='index'),

    # ----------登录、注销----------
    # url(r'^login/$', views.user_login, name='user_login'),  # 自定义的登录
    url(r'^login/$', auth_views.login, name='user_login'),  # django内置登录
    # 以一个字典类型，向默认的auth_views.login传template_name的值
    url(r'new-login/$', auth_views.login, {'template_name': 'account/login.html'}),  # django内置登陆方法2
    # url(r'^logout/$', auth_views.logout, name='user_logout'),  # 默认使用./templates/registration/logged_out.html模板
    url(r'^logout/$', auth_views.logout, {'template_name': 'account/logout.html'}, name='user_logout'),

    # ----------注册----------
    url(r'^register/$', views.register, name='user_register'),

    # ----------修改密码----------
    url(r'^password-change/$', auth_views.password_change, {'post_change_redirect': '/account/password-change-done'},
        name='password_change'),
    url(r'^password-change-done/$', auth_views.password_change_done, name='password_change_done'),

    #  ----------重置密码----------
    url(r'^password-reset/$', auth_views.password_reset, {'template_name': 'account/password_reset_form.html',
                                                          'email_template_name': 'account/password_reset_email.html',
                                                          'subject_template_name': 'account/password_reset_subject.txt',
                                                          'post_reset_redirect': '/account/password-reset-done'},
        name='password_reset'),
    url(r'^password-reset-done/$', auth_views.password_reset_done,
        {'template_name': 'account/password_reset_done.html'}, name='password_reset_done'),
    url(r'^password-reset-confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.password_reset_confirm,
        {'template_name': 'account/password_reset_confirm.html',
         'post_reset_redirect': '/account/password-reset-complete'}, name='password_reset_confirm'),
    url(r'^password-reset-complete/$', auth_views.password_reset_complete,
        {"template_name": "account/password_reset_complete.html"}, name="password_reset_complete"),
]

