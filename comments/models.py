from django.db import models


class Comment(models.Model):
    username = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    homepage = models.URLField(blank=True, null=True)
    text = models.TextField(blank=False, null=False)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}: {self.text}"
