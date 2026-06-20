from django.db import models
from django.utils import timezone
from clients.models import Client


class Message(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.subject


class Mailing(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    recipients = models.ManyToManyField(Client)

    def get_status(self):
        now = timezone.now()

        if now < self.start_time:
            return "Создана"
        elif self.start_time <= now <= self.end_time:
            return "Запущена"
        return "Завершена"

    def __str__(self):
        return f"Mailing {self.id}"
