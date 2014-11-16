from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255, default='My Blog')
    tagline = models.CharField(max_length=255, null=True, blank=True)

    @staticmethod
    def get_unique():
        """
        Returns the only instance of the Blog in the data store.
        If there are no Blog it creates a default one.
        """
        blog, __ = Blog.objects.get_or_create()
        return blog


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
