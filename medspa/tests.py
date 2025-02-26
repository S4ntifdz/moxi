from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from medspa.models.appointment import Appointment
from medspa.models.medspa import Medspa
from medspa.models.service import Service
from medspa.models.service_category import ServiceCategory
from medspa.models.service_product import ServiceProduct
from medspa.models.service_type import ServiceType


class MedspaTests(APITestCase):
    def setUp(self):
        self.medspa = Medspa.objects.create(
            name="Test Medspa",
            address="123 Test St",
            phone_number="+12345678901",
            email="test@medspa.com",
        )

    def test_create_medspa(self):
        url = reverse("medspa-list")
        data = {
            "name": "New Medspa",
            "address": "456 New St",
            "phone_number": "+12345678902",
            "email": "new@medspa.com",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Medspa.objects.count(), 2)


class ServiceTests(APITestCase):
    def setUp(self):
        self.medspa = Medspa.objects.create(
            name="Test Medspa",
            address="123 Test St",
            phone_number="+12345678901",
            email="test@medspa.com",
        )
        self.category = ServiceCategory.objects.create(name="Test Category")
        self.type = ServiceType.objects.create(name="Test Type", category=self.category)
        self.product = ServiceProduct.objects.create(
            name="Test Product", service_type=self.type
        )
        self.service = Service.objects.create(
            name="Test Service",
            description="Test Description",
            price=100.00,
            duration=30,
            medspa=self.medspa,
        )
        
        self.service.product.add(self.product)

    def test_create_service(self):
        url = reverse("service-list")
        data = {
            "name": "New Service",
            "description": "New Description",
            "price": 150.00,
            "duration": 45,
            "medspa": self.medspa.id,
            "product": [self.product.id],
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Service.objects.count(), 2)


class AppointmentTests(APITestCase):
    def setUp(self):
        self.medspa = Medspa.objects.create(
            name="Test Medspa",
            address="123 Test St",
            phone_number="+12345678901",
            email="test@medspa.com",
        )
        self.category = ServiceCategory.objects.create(name="Test Category")
        self.type = ServiceType.objects.create(name="Test Type", category=self.category)
        self.product = ServiceProduct.objects.create(
            name="Test Product", service_type=self.type
        )
        self.service = Service.objects.create(
            name="Test Service",
            description="Test Description",
            price=100.00,
            duration=30,
            medspa=self.medspa,
        )
        
        self.service.product.add(self.product)

    def test_create_appointment(self):
        url = reverse("appointment-list")
        data = {
            "medspa": self.medspa.id,
            "start_time": "2024-03-01T14:30:00Z",
            "services": [self.service.id],
            "status": "scheduled",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Appointment.objects.count(), 1)

    def test_appointment_total_calculations(self):
        appointment = Appointment.objects.create(
            medspa=self.medspa, start_time="2024-03-01T14:30:00Z", status="scheduled"
        )
        appointment.services.add(self.service)

        self.assertEqual(appointment.total_duration, 30)
        self.assertEqual(float(appointment.total_price), 100.00)
