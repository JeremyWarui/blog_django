from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

# Create your models here.


class Author(models.Model):
    """Author model showing the details of the author"""
    name = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(
        max_length=200, help_text='Enter a short bio about the author')

    class Meta:
        """default ordering of the author details"""
        ordering = ['name']

    def __str__(self):
        """returns string representation of the model"""
        return f'{self.name.username}'

    def get_absolute_url(self):
        """returns the url to access a particular author instance"""
        return reverse('author_detail', args=[str(self.pk)])


class Blog(models.Model):
    """Blog model showing the details of the blog"""
    title = models.CharField(max_length=100)
    # Use User model directly
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True)
    content = models.TextField(
        max_length=2000, help_text='Enter the blog content')
    post_date = models.DateField(default=date.today)

    class Meta:
        """default ordering of the blog details"""
        ordering = ['-post_date']

    def __str__(self):
        """returns string representation of the model"""
        return f'{self.title}'

    def get_absolute_url(self):
        """returns the url to access a particular blog instance"""
        return reverse('blog_detail', args=[str(self.pk)])


class Comment(models.Model):
    """Comment model showing the details of the comment"""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=200, help_text='Enter the comment about the blog')

    class Meta:
        """default ordering of the comment details"""
        ordering = ['-post_date']

    def __str__(self):
        """returns string representation of the model"""
        return f'{self.author} on {self.blog}'
