from django.test import TestCase
from django.contrib.auth.models import User
from .models import Author, Blog, Comment
from django.urls import reverse
# Create your tests here.


class AuthorModelTest(TestCase):
    """test case for the author model"""
    def setUp(self):
        """set up the test case"""
        # Create test authors
        self.user1 = User.objects.create(
            username='john_doe',
            password='password123',
        )

        self.user1.save()

        self.author1 = Author.objects.create(
            name=self.user1,
            bio='This is a test bio for John Doe'
        )
        self.user2 = User.objects.create(
            username='jane_doe',
            password='password123',
        )
        self.user2.save()

        self.author2 = Author.objects.create(
            name=self.user2,
            bio='This is a test bio for Jane Doe'
        )

    def test_author_str(self):
        """test the string representation of the author model"""
        self.assertEqual(str(self.author1), "john_doe")
        self.assertEqual(str(self.author2), "jane_doe")

    def test_author_get_absolute_url(self):
        """test that absolute url is the correct url"""
        self.assertEqual(self.author1.get_absolute_url(), reverse(
            'author_detail', args=str(self.author1.pk)))
    
    def test_author_bio(self):
        """test the bio of the author"""
        self.assertEqual(self.author1.bio, "This is a test bio for John Doe")


class BlogModelTest(TestCase):
    """test case for the blog model"""

    def setUp(self):
        """set up the test case"""
        self.user = User.objects.create(
            username='john_doe',
            password='password123',
        )
        self.user.save()

        self.author = Author.objects.create(
            name=self.user,
            bio='This is a test bio for john_doe'
        )
        self.blog = Blog.objects.create(
            title='Test Blog',
            author=self.author,
            content='This is a test blog content'
        )

    def test_blog_str(self):
        """test the string representation of the blog model"""
        self.assertEqual(str(self.blog), "Test Blog")
        self.assertEqual(str(self.blog.author.name), "john_doe")

    def test_blog_get_absolute_url(self):
        """test that absolute url is the correct url"""
        self.assertEqual(self.blog.get_absolute_url(), reverse(
            'blog_detail', args=str(self.blog.pk)))
    
    def test_blog_author(self):
        """test the author of the blog"""
        self.assertEqual(str(self.blog.author), "john_doe")
