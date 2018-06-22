# coding=utf-8

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BlogArticles(models.Model):

    # 标题title属性为CharField()类型，最大字数为300
    title = models.CharField(max_length=300)
    # 作者author规定了文章与用户之间的关系，1个用户对应多个文章的关系，ForeignKey（）就是反应这种“一对多的关系”，类User就是BlogArticles的对应对象
    # related_name="blog_posts"的作用是通过类User反向查询到BlogArticles
    author = models.ForeignKey(User, related_name="blog_posts")
    # 文章内容boby属性为TextField，大文本，巨长的文本
    boby = models.TextField()
    # 发表时间publish属性为DateTimeField，日期+时间，timezone.now当前时区的日期时间
    publish = models.DateTimeField(default=timezone.now)

    # 通过ordering=("-publish",)规定了BlogArticles实例对象的显示顺序，即按照publish字段值得倒序显示。
    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title
# Create your models here.
