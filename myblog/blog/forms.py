from django.forms import ModelForm
from .models import Blog, Comment, Author
# from django import forms

class BlogForm(ModelForm):
    """Form for creating and updating blog instances."""
    pass