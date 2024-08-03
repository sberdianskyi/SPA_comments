from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from comments.forms import CommentForm
from comments.models import Comment


class CommentsListView(generic.ListView):
    model = Comment
    template_name = "comments/index.html"
    context_object_name = "comment_list"
    ordering = ["-created_time"]
    paginate_by = 25


class CommentsCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    success_url = reverse_lazy("comments:comment-list")
    template_name = "comments/comment_form.html"
