from django.contrib import admin

from comments.models import Comment


@admin.register(Comment)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "text"]
