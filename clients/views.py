from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Client
from django.contrib.auth.models import Group


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = "clients/client_list.html"

    def get_queryset(self):
        user = self.request.user

        if user.groups.filter(name="Manager").exists():
            return Client.objects.all()

        return Client.objects.filter(user=user)


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = ["email", "full_name", "comment"]
    success_url = reverse_lazy("client_list")
    template_name = "clients/client_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ["email", "full_name", "comment"]
    success_url = reverse_lazy("client_list")
    template_name = "clients/client_form.html"

    def get_queryset(self):
        return Client.objects.filter(user=self.request.user)


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy("client_list")
    template_name = "clients/client_confirm_delete.html"

    def get_queryset(self):
        return Client.objects.filter(user=self.request.user)
