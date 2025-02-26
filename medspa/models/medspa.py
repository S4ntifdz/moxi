from django.db import models
from django.core.validators import RegexValidator


class Medspa(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    email = models.EmailField()

    def __str__(self):
        return self.name
