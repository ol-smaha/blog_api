from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "votes_amount"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "author", "content"]


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
