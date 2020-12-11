from django.contrib import admin

# Register your models here.
from .models import FeaturedPost

# class FeaturedAdmin(admin.Modeladmin):

admin.site.register(FeaturedPost)