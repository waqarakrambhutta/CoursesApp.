from django.db import models
from django.conf import settings

# Create your models here.
class Author(models.Model):
    phone = models.CharField(max_length=255)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
