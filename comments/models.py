from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    homepage = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.username


class Comment(models.Model):
    user = models.ForeignKey(User,
                             blank=False,
                             null=False,
                             on_delete=models.CASCADE,
                             related_name="comments")
    text = models.TextField(blank=False, null=False)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}: {self.text}"


class Reply(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="replies")
    text = models.TextField(blank=False, null=False)
    created_time = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment,
                                on_delete=models.CASCADE,
                                related_name="replies")

    def __str__(self):
        return f"Reply by {self.user} at {self.created_time}"



