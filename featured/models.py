from django.db import models

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class FeaturedPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='featured/%Y/%m/%d/', max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    url = models.CharField(max_length=200, unique=True, default="none")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
