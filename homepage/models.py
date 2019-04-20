from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    smalltext = models.TextField(max_length=80)

    def __str__(self):
        return "Article: " + self.title
