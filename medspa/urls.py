from django.urls import path, include
from rest_framework.routers import DefaultRouter
from medspa.views.appointment.appointment_view import AppointmentViewSet
from medspa.views.medspas.medspa_view import MedspaViewSet
from medspa.views.services.service_category_view import ServiceCategoryViewSet
from medspa.views.services.service_products_view import ServiceProductViewSet
from medspa.views.services.service_type_view import ServiceTypeViewSet
from medspa.views.services.service_view import ServiceViewSet
from medspa.views.suppliers.supplier_view import SupplierViewSet

router = DefaultRouter()
router.register(r"medspas", MedspaViewSet)
router.register(r"services", ServiceViewSet, basename="service")
router.register(r"appointments", AppointmentViewSet, basename="appointment")
router.register(r"categories", ServiceCategoryViewSet)
router.register(r"types", ServiceTypeViewSet)
router.register(r"products", ServiceProductViewSet)
router.register(r"suppliers", SupplierViewSet)

urlpatterns = [
    path("v1/", include(router.urls)),
]
