from django.db import models

class blog_preview(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    content = models.TextField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
