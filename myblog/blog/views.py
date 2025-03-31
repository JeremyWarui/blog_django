from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from .models import Blog, Comment, Author
from django.contrib.auth.models import User

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

# create a comments form to be viewed


class CommentCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    """View to create a new comment"""
    model = Comment
    fields = ['description']
    permission_required = 'blog.add_comment'
    permission_denied_message = 'You must be logged in to add a comment.'

    def form_valid(self, form):
        # Associate the comment with the blog
        blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        form.instance.blog = blog
        # Associate the comment with the currently logged-in user (User instance)
        form.instance.author = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog_detail', kwargs={'pk': self.object.blog.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return context

# create new blogs
class BlogCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    """View to create a new blog"""
    model = Blog
    fields = ['title', 'content']
    permission_required = 'blog.add_blog'
    permission_denied_message = 'You must be logged in to add a blog.'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('blog_detail', kwargs={'pk': self.object.pk})