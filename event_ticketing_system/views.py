from django.shortcuts import redirect, render, get_object_or_404
from django.utils.dateparse import parse_duration
from events.models import Events, EventType
from django.utils import timezone
from datetime import datetime, timedelta
from tickets.models import Profile

from django.contrib.auth.decorators import login_required


# @login_required
# def index(request):
#     user_profile = Profile.objects.get(user=request.user)
#     return render(request, 'index.html',{'user_type':user_profile.user_type})

@login_required 
def index(request):
    try:
        user_profile = Profile.objects.get(user=request.user)
        return render(request, 'index.html', {'user_type': user_profile.user_type})
    except Profile.DoesNotExist:
        # Handle the case where the profile does not exist
        return redirect('register')  # or another appropriate view
    
    
#def index(request):
  #  return render(request, "index.html")

def home(request):
    return render(request, "home.html")

def footer(request):
    return render(request, "footer.html")

def header(request):
    return render(request, "header.html")

def eventlist(request):
    events = Events.objects.all()
    return render(request, "eventlist.html", {'events': events})

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def admindashboard(request):
    return render(request, "admindashboard.html")


def event_details(request, name):
    event = get_object_or_404(Events, name=name)
    return render(request, 'event_details.html', {'event': event})

@login_required
def addevent(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        event_time_str = request.POST['event_time']
        book_time_str = request.POST['book_time']
        pricings = request.POST['priciings']
        instructions = request.POST['instructions']
        event_type_name = request.POST['event_type']
        created_date_str = request.POST['created_date']

        # Parse prep_time and cook_time strings into timedelta objects
        event_time = parse_duration(event_time_str)
        book_time = parse_duration(book_time_str)

        # Ensure RecipeType instance exists or create a new one
        event_type, created = EventType.objects.get_or_create(name=event_type_name)

        # Parse created_date string into datetime object
        try:
            created_date = datetime.strptime(created_date_str, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            created_date = timezone.now()

        event = Events(
            name=name,
            description=description,
            event_time=event_time,
            book_time=book_time,
            pricings=pricings,
            instructions=instructions,
            event_type=event_type,
            created_date=created_date
        )
        event.save()
        return render(request, 'success.html', {'event': event})

    return render(request, 'addevent.html')