import requests
import json
from pprint import pprint

BASE_URL = 'http://localhost:8000'

def make_request(method, endpoint, data=None):
    url = f"{BASE_URL}{endpoint}"
    headers = {'Content-Type': 'application/json'}
    try:
        if method == 'GET':
            response = requests.get(url)
        elif method == 'POST':
            response = requests.post(url, data=json.dumps(data), headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Test create_event
print("Creating an event...")
event_data = {
    'name': 'Summer Music Festival',
    'start_date': '2024-07-15T14:00:00Z',
    'description': 'A fantastic summer music festival',
    'location': 'Central Park, New York'
}
event_response = make_request('POST', '/events/create/', event_data)
print(json.dumps(event_response))
if event_response:
    event_id = event_response.get('event_id')
    print(f"Event created successfully with ID: {event_id}")
else:
    print("Failed to create event")
    exit()

# Test list_events
print("\nListing all events...")
events_response = make_request('GET', '/events/')
if events_response:
    print("Events:")
    pprint(events_response)
else:
    print("Failed to list events")

# Test create_ticket
print("\nCreating a ticket for the event...")
ticket_data = {
    'name': 'General Admission',
    'price': '50.00',
    'description': 'General admission ticket',
    'quantity': 1000,
    'start_date': '2024-07-15T14:00:00Z',
    'end_date': '2024-07-15T23:00:00Z',
    'type': 'general'
}
ticket_response = make_request('POST', f'/events/{event_id}/tickets/create/', ticket_data)
# print(ticket_response)
if ticket_response:
    ticket_id = ticket_response.get('ticket_id')
    print(f"Ticket created successfully with ID: {ticket_id}")
else:
    print("Failed to create ticket")
    exit()

# Test create_booking
print("\nCreating a booking...")
booking_data = {
    'ticket_id': ticket_id,
    'quantity': 2,
    'payment_method': 'credit_card',
    'payment_currency': 'USD',
    'username': 'admin',
    'password': 'admin123'
}
booking_response = make_request('POST', '/bookings/create/', booking_data)
print(booking_response)
if booking_response:
    booking_id = booking_response.get('booking_id')
    print(f"Booking created successfully with ID: {booking_id}")
else:
    print("Failed to create booking")

print("\nAPI testing completed.")