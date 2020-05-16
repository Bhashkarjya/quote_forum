from django.db import models

# Create your models here.
class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=15)
    def __str__(self):
        return str(self.quote)
