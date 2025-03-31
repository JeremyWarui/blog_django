from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog, Comment, Author

# Create your views here.


def index(request):
    """View function to render the index page"""
    num_of_blogs = Blog.objects.count()
    num_of_authors = Author.objects.count()
    num_of_comments = Comment.objects.count()

    context = {
        'num_of_blogs': num_of_blogs,
        'num_of_authors': num_of_authors,
        'num_of_comments': num_of_comments,
    }

    return render(request, 'index.html', context=context)

class BlogListView(ListView):
    """View to display blogs"""
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 5

class BlogDetailView(DetailView):
    """View to display blog details"""
    model = Blog

class AuthorListView(ListView):
    """View to display authors"""
    model = Author
    paginate_by = 5
    context_object_name = 'authors'

class AuthorDetailsView(DetailView):
    """View to display author details"""
    model = Author
