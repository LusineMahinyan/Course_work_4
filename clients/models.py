from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="clients"
    )

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.email
