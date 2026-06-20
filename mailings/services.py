from django.core.mail import send_mail
from django.utils import timezone
from attempts.models import Attempt


def send_mailing(mailing):
    now = timezone.now()

    # 1. проверка времени (КРИТЕРИЙ)
    if not (mailing.start_time <= now <= mailing.end_time):
        raise Exception("Рассылка недоступна по времени")

    attempts = []

    # 2. отправка каждому клиенту
    for client in mailing.recipients.all():
        try:
            send_mail(
                subject=mailing.message.subject,
                message=mailing.message.body,
                from_email="admin@example.com",
                recipient_list=[client.email],
                fail_silently=False,
            )

            attempts.append(Attempt(
                mailing=mailing,
                status="success",
                server_response="Письмо отправлено"
            ))

        except Exception as e:
            attempts.append(Attempt(
                mailing=mailing,
                status="failed",
                server_response=str(e)
            ))

    # 3. batch создание (ОБЯЗАТЕЛЬНО ПО ТЗ)
    Attempt.objects.bulk_create(attempts)
