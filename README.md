# Event Booking App

This is a Django-based Event Booking application that allows users to create events, manage tickets, and make bookings.

## Features

- Create and list events
- Create tickets for events
- Make bookings for tickets
- User authentication for bookings

## Technologies Used

- Django
- Python
- SQLite (default database)

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/event-booking-app.git
cd event-booking-app
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

3. Install the required packages:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```


The application should now be running at `http://localhost:8000`.

## API Endpoints

- Create Event: POST `/events/create/`
- List Events: GET `/events/`
- Create Ticket: POST `/events/<event_id>/tickets/create/`
- Create Booking: POST `/bookings/create/`

## Testing

To run the API tests:

1. Ensure the Django server is running.
2. Run the test script:
```bash
python tests.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)