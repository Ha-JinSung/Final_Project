# Django의 기본 모듈과 사용자 모델, 그리고 RichTextField를 위한 ckeditor 모듈을 임포트합니다.
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumb_image = models.ImageField(
        upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(
        upload_to='blog/files/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    view_count = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    user  = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    content = RichTextField()
    
    def __str__(self):
        return self.message
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Reply(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='reply'
    )
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='replies'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.message
