from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import BlogArticles
from django.http import HttpResponse
from django.template import RequestContext, loader


# index视图（测试用）
def index(request):
    # return HttpResponse("Hello, world. You're at the blog index.")  # 返回提示

    # 如果想在主页显示文章，需要如下修改（参照下面的blog_title视图）
    blogs = BlogArticles.objects.all()
    return render(request, "index.html", {"blogs": blogs})


def blog_title(request):
    """响应用户请求，展示文章标题"""
    blogs = BlogArticles.objects.all()
    # render：将数据渲染到模板上
    return render(request, "blog/titles.html", {"blogs": blogs})


def blog_article(request, article_id):
    # article = BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(BlogArticles, id=article_id)  # 对异常请求进行处理
    pub = article.publish
    return render(request, "blog/content.html", {"article": article, "publish": pub})
