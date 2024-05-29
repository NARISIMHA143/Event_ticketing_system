from django.urls import path 

from . import views
from .views import event_details




urlpatterns = [

    path('event_details/', event_details, name='event_details'),
]