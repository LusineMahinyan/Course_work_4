from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Mailing


class MailingListView(ListView):
    model = Mailing
    template_name = "mailings/mailing_list.html"


class MailingCreateView(CreateView):
    model = Mailing
    fields = ["start_time", "end_time", "message", "recipients"]
    success_url = reverse_lazy("mailing_list")
    template_name = "mailings/mailing_form.html"


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ["start_time", "end_time", "message", "recipients"]
    success_url = reverse_lazy("mailing_list")
    template_name = "mailings/mailing_form.html"


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy("mailing_list")
    template_name = "mailings/mailing_confirm_delete.html"
    