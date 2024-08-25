import json
# import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404
from .models import Event, Ticket, Booking
from django.contrib.auth import authenticate


@require_POST
@csrf_exempt
def createEvent(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # print(data)
            newEvent = Event.objects.create(
                name=data.get('name'),
                description=data.get('description'),
                start_date=data.get('start_date'),
                location=data.get('location'),
            )
            if newEvent:
                return JsonResponse({'message': 'Event created successfully', 'event_id': newEvent.event_id})
            return JsonResponse({'message': 'Failed to create event'})
        except Exception as e:
            return JsonResponse({'message': f'Failed to create event: {str(e)}'}, status=400)
    
    else:
        return JsonResponse({'message': 'Invalid request method'})


@require_GET
def listEvents(request):
    events = Event.objects.all()
    events_data = serialize('json', events)
    return JsonResponse({'events': json.loads(events_data)})


@require_POST
@csrf_exempt
def createTicket(request, event_id):
    try:
        event = get_object_or_404(Event, event_id=event_id)
        data = json.loads(request.body)
        new_ticket = Ticket.objects.create(
            event=event,
            name=data.get('name'),
            price=data.get('price'),
            description=data.get('description'),
            quantity=data.get('quantity'),
            start_date=data.get('start_date'),
            end_date=data.get('end_date'),
            type=data.get('type')
        )
        return JsonResponse({'message': 'Ticket created successfully', 'ticket_id': new_ticket.ticket_id})
    except Exception as e:
        return JsonResponse({'message': f'Failed to create ticket: {str(e)}'}, status=400)


@require_POST
@csrf_exempt
def createBooking(request):
    try:
        data = json.loads(request.body)
        ticket = get_object_or_404(Ticket, ticket_id=data.get('ticket_id'))
        
        username = data.get('username')
        password = data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if ticket.quantity < data.get('quantity'):
            return JsonResponse({'message': 'Not enough tickets available'}, status=400)
        
        total_price = ticket.price * data.get('quantity')
        
        new_booking = Booking.objects.create(
            ticket=ticket,
            user=user,
            quantity=data.get('quantity'),
            total_price=float(total_price),
            status='PENDING',
            payment_method=data.get('payment_method'),
            payment_status='PENDING',
            payment_amount=float(total_price),
            payment_currency=data.get('payment_currency', 'USD')
        )
        
        # Update ticket quantity
        ticket.quantity -= data.get('quantity')
        ticket.save()
        
        return JsonResponse({'message': 'Booking created successfully', 'booking_id': new_booking.booking_id})
    except Exception as e:
        return JsonResponse({'message': f'Failed to create booking: {str(e)}'})