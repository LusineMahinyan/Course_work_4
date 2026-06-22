from django.views.generic import TemplateView
from django.core.cache import cache
from django.utils import timezone

from mailings.models import Mailing
from clients.models import Client
from attempts.models import Attempt


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cached_data = cache.get("home_stats")

        if not cached_data:
            now = timezone.now()

            cached_data = {
                "mailings_count": Mailing.objects.count(),
                "clients_count": Client.objects.count(),
                "active_mailings": Mailing.objects.filter(
                    start_time__lte=now,
                    end_time__gte=now
                ).count(),
                "success_attempts": Attempt.objects.filter(status="success").count(),
                "failed_attempts": Attempt.objects.filter(status="failed").count(),
            }

            cache.set("home_stats", cached_data, 60)  # 60 секунд кеш

        context.update(cached_data)
        return context
