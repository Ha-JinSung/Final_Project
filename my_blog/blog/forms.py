from django import forms
from .models import Post, Comment, Tag, Reply

class PostForm(forms.ModelForm):
    tags = forms.CharField()

    class Meta:
        model = Post
        fields = ['title', 'content', 'thumb_image', 'file_upload', 'tags'] 

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.save()
        return instance


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['message']