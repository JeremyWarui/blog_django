from django.test import TestCase
from .models import Author, Blog, Comment
from django.urls import reverse
# Create your tests here.


class AuthorModelTest(TestCase):
    """test case for the author model"""
    def setUp(self):
        """set up the test case"""
        # Create test authors
        self.author1 = Author.objects.create(
            first_name='John',
            last_name='Doe',
            user_name='john_doe',
            bio='This is a test bio for John Doe'
        )
        self.author2 = Author.objects.create(
            first_name='Jane',
            last_name='Doe',
            user_name='jane_doe',
            bio='This is a test bio for Jane Doe'
        )

    def test_author_str(self):
        """test the string representation of the author model"""
        self.assertEqual(str(self.author1), "Doe, John")
        self.assertEqual(str(self.author2), "Doe, Jane")

    def test_author_get_absolute_url(self):
        """test that absolute url is the correct url"""
        self.assertEqual(self.author1.get_absolute_url(), reverse(
            'author_detail', args=str(self.author1.pk)))
    


class BlogModelTest(TestCase):
    """test case for the blog model"""

    def setUp(self):
        """set up the test case"""
        self.author = Author.objects.create(
            first_name='John',
            last_name='Doe',
            user_name='john_doe',
            bio='This is a test bio for John Doe'
        )
        self.blog = Blog.objects.create(
            title='Test Blog',
            author=self.author,
            content='This is a test blog content'
        )

    def test_blog_str(self):
        """test the string representation of the blog model"""
        self.assertEqual(str(self.blog), "Test Blog by Doe, John")
        self.assertEqual(str(self.blog.author.user_name), "john_doe")

    def test_blog_get_absolute_url(self):
        """test that absolute url is the correct url"""
        self.assertEqual(self.blog.get_absolute_url(), reverse(
            'blog_detail', args=str(self.blog.pk)))
    
    def test_new_blog_created(self):
        pass