from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    usable_password = models.BooleanField(default=True)
    pass
