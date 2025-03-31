from django.contrib import admin
from .models import Blog, Comment, Author


# define the admin interface for the Author model
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'user_name')
    list_filter = ('last_name',)
    fields = ('first_name', 'last_name', 'user_name', 'bio')


class CommentsInline(admin.TabularInline):
    model = Comment
    fields = ('blog', 'posted_at', 'author', 'description')
    readonly_fields = ('posted_at',)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_date')
    list_filter = ('post_date',)
    fields = ('title', 'author', 'content', 'post_date')
    readonly_fields = ('post_date',)
    inlines = [CommentsInline]


# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('blog', 'posted_at', 'author')
#     list_filter = ('posted_at',)
#     fields = ('blog', 'posted_at', 'author', 'description')

# Register the models

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
admin.site.register(Author, AuthorAdmin)
