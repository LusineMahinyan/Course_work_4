from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required
from .models import Mailing
from django.http import HttpResponseForbidden
from django.core.cache import cache


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    template_name = "mailings/mailing_list.html"

    def get_queryset(self):
        user = self.request.user
        cache_key = f"mailings_{user.id}"

        mailings = cache.get(cache_key)

        if not mailings:
            mailings = Mailing.objects.filter(user=user)
            cache.set(cache_key, mailings, 60)

        return mailings


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    fields = ["start_time", "end_time", "message", "recipients"]
    success_url = reverse_lazy("mailing_list")
    template_name = "mailings/mailing_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    fields = ["start_time", "end_time", "message", "recipients"]
    success_url = reverse_lazy("mailing_list")
    template_name = "mailings/mailing_form.html"

    def get_queryset(self):
        return Mailing.objects.filter(user=self.request.user)


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy("mailing_list")
    template_name = "mailings/mailing_confirm_delete.html"

    def get_queryset(self):
        return Mailing.objects.filter(user=self.request.user)

@login_required
def run_mailing(request, pk):
    mailing = get_object_or_404(Mailing, pk=pk)

    if mailing.user != request.user:
        return HttpResponseForbidden("Нет доступа")


    return redirect("mailing_list")