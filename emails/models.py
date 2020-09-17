from django.db import models

# Create your models here.
class EmailEntry(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=120, blank=True)
    updated = models.DateTimeField(auto_now=True) # sets when saved
    timestamp = models.DateTimeField(auto_now_add=True) # sets when added
