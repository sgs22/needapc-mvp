from django.shortcuts import render
from django.http import HttpResponse, Http404

from.models import EmailEntry

# Create your views here.
# Model -> View -> Template

def email_entry_get_view(request, id=None, *args, **kwargs):
    # get a single item stored in the db
    # print(args, kwargs)
    #obj = EmailEntry.objects.get(id=id)
    try:
        obj = EmailEntry.objects.get(id=id)
    except EmailEntry.DoesNotExist:
        raise Http404

    return HttpResponse(f"<h1>Hello {obj.email}</h1>")

# def email_entry_list_view():

#     return

# def email_entry_create_view():

#     return
# def email_entry_update_view():

#     return