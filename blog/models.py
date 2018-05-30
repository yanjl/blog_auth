from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=300, verbose_name='标题')
    body = models.TextField(verbose_name='内容')
    publish = models.DateTimeField(default=timezone.now, verbose_name='发布日期')
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='所有者')

    class Meta:
        ordering = ['-publish']
        verbose_name = '帖子'
        verbose_name_plural = '帖子'

    def __str__(self):
        return self.title
