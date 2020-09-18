from django.shortcuts import render
from django.http import HttpResponse, Http404

from .forms import EmailEntryForm
from .models import EmailEntry


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

    return render(request, "get.html", {"object":obj})

# def email_entry_list_view():

#     return

def email_entry_create_view(request, *args, **kwargs):
    print(request.user, request.user.is_authenticated) # is_authenticated()
    form = EmailEntryForm(request.POST or None)
    if form.is_valid():
        # obj = form.save(commit=False) #Model Instance
        # obj.save()
        # new_id = obj.id

        form.save()
        form = EmailEntryForm()
    
    return render(request, "form.html", {"form":form})
# def email_entry_update_view():

#     return