from django.contrib import admin

from .models import Bloggers, Blogs, Genre, Comment

admin.site.register(Genre)
admin.site.register(Bloggers)
admin.site.register(Comment)


class CommentsInline(admin.TabularInline):
    model = Comment
    max_num = 0


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'bloggers', 'genre')
    inlines = [CommentsInline]
