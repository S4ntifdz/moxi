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
- `GET /api/v1/medspas/` - List all medspas
- `POST /api/v1/medspas/` - Create a new medspa
- `GET /api/v1/medspas/{id}/` - Retrieve a specific medspa
- `PUT /api/v1/medspas/{id}/` - Update a medspa
- `DELETE /api/v1/medspas/{id}/` - Delete a medspa

### Services
- `GET /api/v1/services/` - List all services
- `POST /api/v1/services/` - Create a new service
- `GET /api/v1/services/{id}/` - Retrieve a specific service
- `PUT /api/v1/services/{id}/` - Update a service
- `DELETE /api/v1/services/{id}/` - Delete a service
- Query parameters:
  - `medspa` - Filter services by medspa ID
  - `search` - Search services by name or description

### Appointments
- `GET /api/v1/appointments/` - List all appointments
- `POST /api/v1/appointments/` - Create a new appointment
- `GET /api/v1/appointments/{id}/` - Retrieve a specific appointment
- `PUT /api/v1/appointments/{id}/` - Update an appointment
- `DELETE /api/v1/appointments/{id}/` - Delete an appointment
- Query parameters:
  - `status` - Filter by appointment status (scheduled/completed/canceled)
  - `date` - Filter by date (YYYY-MM-DD)

### Service Categories
- `GET /api/v1/categories/` - List all service categories
- `POST /api/v1/categories/` - Create a new category
- Similar endpoints for types, products, and suppliers

## Example API Usage

### Creating a Medspa

```bash
curl -X POST http://localhost:8000/api/v1/medspas/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Luxury Medspa",
    "address": "123 Main St, City, Country",
    "phone_number": "+1234567890",
    "email": "contact@luxurymedspa.com"
  }'
```

### Updating a Medspa

```bash
curl -X PUT http://localhost:8000/api/v1/medspas/{id}/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Luxury Medspa Updated",
    "address": "456 New St, City, Country",
    "phone_number": "+1234567891",
    "email": "newcontact@luxurymedspa.com"
  }'
```

### Deleting a Medspa

```bash
curl -X DELETE http://localhost:8000/api/v1/medspas/{id}/
```

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
    "product": [1]  
  }'
```

### Updating a Service

```bash
curl -X PUT http://localhost:8000/api/v1/services/{id}/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated Botox Treatment",
    "description": "Updated description for Botox",
    "price": "449.99",
    "duration": 45,
    "medspa": 1,
    "product": [1]
  }'
```

### Deletig a Service
```bash
curl -X DELETE http://localhost:8000/api/v1/services/{id}/
```

### Listing All Services for a Specific Medspa
```bash
curl http://localhost:8000/api/v1/services/?medspa={medspa_id}
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

### Updating an Appointment
```bash
curl -X PATCH http://localhost:8000/api/v1/appointments/{appointment_id}/ \
  -H "Content-Type: application/json" \
  -d '{
    "status": "completed",
    "services": [{service_id1}, {service_id2}]
  }'
```

### Listing All Appointments
```bash
curl http://localhost:8000/api/v1/appointments/
```

### Filtering Appointments by Status

```bash
# Get all completed appointments
curl http://localhost:8000/api/v1/appointments/?status=completed
```
### Filtering Appointments by Date

```bash
# Get appointments for a specific date
curl http://localhost:8000/api/v1/appointments/?date=2024-03-01
```
