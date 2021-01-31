from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    mobile_number = models.CharField(max_length=10, unique=True, null=False)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username
        