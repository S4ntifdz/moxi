from django.core.management.base import BaseCommand

from medspa.models.service_category import ServiceCategory
from medspa.models.service_product import ServiceProduct
from medspa.models.service_type import ServiceType
from medspa.models.supplier import Supplier


class Command(BaseCommand):
    help = "Load initial service data"

    def handle(self, *args, **kwargs):
        # Create service categories
        categories = {
            "Injectables": {
                "types": {
                    "Neuromodulators": {
                        "products": [
                            {"name": "Botox", "supplier": "Allergan"},
                            {"name": "Daxxify", "supplier": "Revance"},
                            {"name": "Xeomin", "supplier": "Merz"},
                        ]
                    },
                    "HA Dermal Filler": {
                        "products": [
                            {"name": "Juvederm Ultra", "supplier": "Allergan"},
                            {"name": "Restylane", "supplier": "Galderma"},
                            {"name": "Belotero", "supplier": "Merz"},
                        ]
                    },
                    "Calcium Hydroxyapatite": {
                        "products": [
                            {"name": "Radiesse", "supplier": "Merz"},
                        ]
                    },
                }
            },
            "Chemical Peels": {
                "types": {
                    "Light Chemical Peel": {
                        "products": [
                            {"name": "Glycolic Acid Peel", "supplier": None},
                            {"name": "Salicylic Acid Peel", "supplier": None},
                        ]
                    },
                    "Medium Chemical Peel": {
                        "products": [
                            {"name": "TCA Peel", "supplier": None},
                        ]
                    },
                }
            },
        }

        # Create suppliers first
        suppliers = {}
        supplier_names = ["Allergan", "Revance", "Merz", "Galderma"]
        for supplier_name in supplier_names:
            supplier, created = Supplier.objects.get_or_create(name=supplier_name)
            suppliers[supplier_name] = supplier
            if created:
                self.stdout.write(f"Created supplier: {supplier_name}")

        # Create categories, types, and products
        for category_name, category_data in categories.items():
            category, created = ServiceCategory.objects.get_or_create(
                name=category_name
            )
            if created:
                self.stdout.write(f"Created category: {category_name}")

            for type_name, type_data in category_data["types"].items():
                service_type, created = ServiceType.objects.get_or_create(
                    name=type_name, category=category
                )
                if created:
                    self.stdout.write(f"Created service type: {type_name}")

                for product_data in type_data["products"]:
                    supplier = (
                        suppliers.get(product_data["supplier"])
                        if product_data["supplier"]
                        else None
                    )
                    product, created = ServiceProduct.objects.get_or_create(
                        name=product_data["name"],
                        service_type=service_type,
                        supplier=supplier,
                    )
                    if created:
                        self.stdout.write(f'Created product: {product_data["name"]}')
