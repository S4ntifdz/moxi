# Moxie Medspa Service Management API

This is a Django-based REST API for managing medspa services and appointments.

## Features

- CRUD operations for Medspas
- Service management with categories, types, and products
- Appointment scheduling with multiple services
- Filtering appointments by status and date

## Prerequisites

- Python 3.8+
- PostgreSQL
- pip

## Setup

1. Create a virtual environment and activate it:
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up PostgreSQL:
- Install PostgreSQL if you haven't already
- Create a database named 'moxie_db'
- Update the database settings in `moxie/settings.py` if needed

4. Apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

### Medspas
- `GET /api/medspas/` - List all medspas
- `POST /api/medspas/` - Create a new medspa
- `GET /api/medspas/{id}/` - Retrieve a specific medspa
- `PUT /api/medspas/{id}/` - Update a medspa
- `DELETE /api/medspas/{id}/` - Delete a medspa

### Services
- `GET /api/services/` - List all services
- `POST /api/services/` - Create a new service
- `GET /api/services/{id}/` - Retrieve a specific service
- `PUT /api/services/{id}/` - Update a service
- `DELETE /api/services/{id}/` - Delete a service
- Query parameters:
  - `medspa` - Filter services by medspa ID
  - `search` - Search services by name or description

### Appointments
- `GET /api/appointments/` - List all appointments
- `POST /api/appointments/` - Create a new appointment
- `GET /api/appointments/{id}/` - Retrieve a specific appointment
- `PUT /api/appointments/{id}/` - Update an appointment
- `DELETE /api/appointments/{id}/` - Delete an appointment
- Query parameters:
  - `status` - Filter by appointment status (scheduled/completed/canceled)
  - `date` - Filter by date (YYYY-MM-DD)

### Service Categories
- `GET /api/categories/` - List all service categories
- `POST /api/categories/` - Create a new category
- Similar endpoints for types, products, and suppliers

## Example API Usage

### Creating a Service

```bash
curl -X POST http://localhost:8000/api/v1/services/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Botox Treatment",
    "description": "FDA-approved treatment for wrinkles",
    "price": "399.99",
    "duration": 30,
    "medspa": 1,
    "product": 1
  }'
```

### Creating an Appointment

```bash
curl -X POST http://localhost:8000/api/v1/appointments/ \
  -H "Content-Type: application/json" \
  -d '{
    "medspa": 1,
    "start_time": "2024-03-01T14:30:00Z",
    "services": [1, 2],
    "status": "scheduled"
  }'
```

### Filtering Appointments

```bash
# Get all completed appointments
curl http://localhost:8000/api/v1/appointments/?status=completed

# Get appointments for a specific date
curl http://localhost:8000/api/v1/appointments/?date=2024-03-01
```
