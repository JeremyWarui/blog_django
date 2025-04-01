from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blogs/<int:pk>', views.BlogDetailView.as_view(), name='blog_detail'),
    path('blogs/create', views.BlogCreateView.as_view(), name='create_blog'),
    path('blogs/<int:pk>/comments/new', views.CommentCreateView.as_view(), name='new_comment'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>', views.BlogListbyAuthorView.as_view(), name='author_detail'),
]
