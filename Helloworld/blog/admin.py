from django.contrib import admin

# Register your models here.

# 将BlogArticles类引入当前环境
from .models import BlogArticles


# 为了丰富管理员列表中的信息，定义一个新类
class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish")
    list_filter = ("publish", "author")
    search_fields = ("title", "body")
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ["publish", "author"]


# 将BlogArticles类注册到admin中
admin.site.register(BlogArticles, BlogArticlesAdmin)
