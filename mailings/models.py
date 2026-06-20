from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from clients.models import Client


class Message(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.subject


class Mailing(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="mailings"
    )

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    recipients = models.ManyToManyField(Client)

    def status(self):
        now = timezone.now()

        if now < self.start_time:
            return "Создана"
        elif self.start_time <= now <= self.end_time:
            return "Запущена"
        return "Завершена"

    def __str__(self):
        return f"Mailing {self.id}"
