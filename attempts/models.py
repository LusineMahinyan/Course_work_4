from django.db import models


class Attempt(models.Model):
    STATUS_CHOICES = [
        ("success", "Успешно"),
        ("failed", "Не успешно"),
    ]

    attempt_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    server_response = models.TextField()

    mailing = models.ForeignKey('mailings.Mailing', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.status} - {self.attempt_time}"

