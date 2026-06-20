from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Client


class ClientListView(ListView):
    model = Client
    template_name = "clients/client_list.html"


class ClientCreateView(CreateView):
    model = Client
    fields = ["email", "full_name", "comment"]
    success_url = reverse_lazy("client_list")
    template_name = "clients/client_form.html"


class ClientUpdateView(UpdateView):
    model = Client
    fields = ["email", "full_name", "comment"]
    success_url = reverse_lazy("client_list")
    template_name = "clients/client_form.html"


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy("client_list")
    template_name = "clients/client_confirm_delete.html"
