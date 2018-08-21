from django.db import models

# Create your models here.

class Camp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    title = models.CharField(max_length=100, blank=True, default='')
    venue = models.TextField()
    openToAll = models.BooleanField(default=False)

    class Meta:
        ordering = ('date',)
