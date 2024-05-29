"""
URL configuration for event_ticketing_system project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path, include,re_path
from django.conf.urls.static import static 
from django.conf import settings 
from django.contrib.auth import views as auth_views


from .views import index, header, footer, eventlist, login, register, addevent, event_details,admindashboard, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', index, name='index'),
    path('header/', header, name='header'),
    path('footer/', footer, name='footer'),
    path('eventlist/', eventlist, name='eventlist'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('admindashboard/', admindashboard, name='admindashboard'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('addevent/', addevent, name='addevent'),
    path('events/', include('events.urls')),
    path('tickets/', include('tickets.urls')),  # Ensure this is correct
    path('event_details/', event_details, name='event_details'),
    #re_path(r'^.*$', index, name='index'),

]

# Append the static files serving
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)