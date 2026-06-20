from django.urls import path
from .views import *

urlpatterns = [
    path("", MailingListView.as_view(), name="mailing_list"),
    path("create/", MailingCreateView.as_view(), name="mailing_create"),
    path("update/<int:pk>/", MailingUpdateView.as_view(), name="mailing_update"),
    path("delete/<int:pk>/", MailingDeleteView.as_view(), name="mailing_delete"),
]
