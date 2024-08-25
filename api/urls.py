from django.urls import path
from .views import createEvent, listEvents, createTicket, createBooking

urlpatterns = [
    path('events/create/', createEvent, name='createEvent'),
    path('events/', listEvents, name='listEvents'),
    path('events/<int:event_id>/tickets/create/', createTicket, name='createTicket'),
    path('bookings/create/', createBooking, name='createBooking'),
]