from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from comments.views import CommentsListView, CommentsCreateView

urlpatterns = [
    path("", CommentsListView.as_view(), name="comment-list"),
    path("comment/create/", CommentsCreateView.as_view(), name="comment-create"),
]

app_name = "comments"
