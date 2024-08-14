from django.contrib import admin

from comments.models import Comment, Reply, User


@admin.register(Comment)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "user_email", "text"]

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = "Email"


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ["user", "user_email", "text"]

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = "Email"


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "homepage"]
