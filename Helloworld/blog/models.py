from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    # 在django2.0后，定义外键和一对一关系的时候需要加on_delete选项，
    # 此参数为了避免两个表里的数据不一致问题，不然会报错
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        # ordering规定了BlogArticle实例对象的显示顺序
        ordering = ("-publish",)

    def __str__(self):
        return self.title