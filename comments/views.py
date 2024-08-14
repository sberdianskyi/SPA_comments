from django.urls import reverse, reverse_lazy
from django.views import generic

from comments.forms import CommentForm, ReplyForm
from comments.models import Comment


class CommentsListView(generic.ListView):
    model = Comment
    template_name = "comments/index.html"
    context_object_name = "comment_list"
    ordering = ["-created_time"]
    paginate_by = 25


class CommentsCreateView(generic.CreateView):
    form_class = CommentForm
    success_url = reverse_lazy("comments:comment-list")
    template_name = "comments/comment_form.html"


class ReplyCreateView(generic.CreateView):
    form_class = ReplyForm
    success_url = reverse_lazy("comments:comment-list")
    template_name = "comments/reply_form.html"

    def form_valid(self, form):
        comment_id = self.kwargs['comment_id']
        comment = Comment.objects.get(id=comment_id)
        form.instance.comment = comment

        return super().form_valid(form)
