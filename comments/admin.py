from django.contrib import admin

from comments.models import User, Post, Comment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "homepage"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "text"]


@admin.register(Comment)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["owner", "text", "post"]
