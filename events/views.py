

# Create your views here.
from django.shortcuts import render,get_object_or_404

# Create your views here.

from .models import Events


def event_details(request, name):
    event = get_object_or_404(event,name=name)
    return render(request, 'event_details.html',{'event':event})
