from django.db import models
from django.urls import reverse

# Create your models here.


class Author(models.Model):
    """Author model showing the details of the author"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    bio = models.TextField(max_length=200)

    class Meta:
        """default ordering of the author details"""
        ordering = ['last_name', 'first_name']

    def __str__(self):
        """returns string representation of the model"""
        return f'{self.last_name}, {self.first_name}'

    def get_absolute_url(self):
        """returns the url to access a particular author instance"""
        return reverse('author_detail', args=[str(self.pk)])


class Blog(models.Model):
    """Blog model showing the details of the blog"""
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """default ordering of the blog details"""
        ordering = ['-post_date']

    def __str__(self):
        """returns string representation of the model"""
        return f'{self.title} by {self.author}'

    def get_absolute_url(self):
        """returns the url to access a particular blog instance"""
        return reverse('blog_detail', args=[str(self.pk)])


class Comment(models.Model):
    """Comment model showing the details of the comment"""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

    class Meta:
        """default ordering of the comment details"""
        ordering = ['-posted_at']

    def __str__(self):
        """returns string representation of the model"""
        return f'{self.author} on {self.blog}'
