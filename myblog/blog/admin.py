from django.contrib import admin
from .models import Blog, Comment, Author


# define the admin interface for the Author model
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
    fields = ('name', 'bio')


class CommentsInline(admin.TabularInline):
    model = Comment
    fields = ('blog', 'post_date', 'author', 'description')
    readonly_fields = ('post_date',)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_date')
    list_filter = ('post_date',)
    fields = ('title', 'author', 'content', 'post_date')
    readonly_fields = ('post_date',)
    inlines = [CommentsInline]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'post_date', 'author')
    list_filter = ('post_date',)
    fields = ('blog', 'post_date', 'author', 'description')

# Register the models

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Author, AuthorAdmin)
