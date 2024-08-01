from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    homepage = models.URLField()


class Post(models.Model):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name="posts"
                              )
    text = models.CharField(max_length=255, blank=False, null=False)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{User.username} posted at {self.created_time}"


class Commentary(models.Model):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name="comments"
                              )
    text = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="posts")

    def __str__(self):
        return f"{User.username}: {self.text}"
