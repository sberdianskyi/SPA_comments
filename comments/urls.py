from django.urls import path

from comments.views import CommentsListView, CommentsCreateView, ReplyCreateView

urlpatterns = [
    path("", CommentsListView.as_view(), name="comment-list"),
    path("comment/create/", CommentsCreateView.as_view(), name="comment-create"),
    path("reply/create/<int:comment_id>/", ReplyCreateView.as_view(), name="reply-create"),
]

app_name = "comments"
