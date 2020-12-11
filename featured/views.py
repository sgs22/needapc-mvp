from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404


from .models import FeaturedPost

# Rendering template with query on all featured posts
def featured_view(request, id=None, *args, **kwargs):
    queryset = FeaturedPost.objects.filter(status=1).order_by('-created_on')
    return render(request, "featured/index.html", {"featured_list": queryset})

