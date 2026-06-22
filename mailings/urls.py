from django.urls import path
from .views import (
    MailingListView,
    MailingCreateView,
    MailingUpdateView,
    MailingDeleteView,
    run_mailing,
)


urlpatterns = [
    path("", MailingListView.as_view(), name="mailing_list"),
    path("create/", MailingCreateView.as_view(), name="mailing_create"),
    path("update/<int:pk>/", MailingUpdateView.as_view(), name="mailing_update"),
    path("delete/<int:pk>/", MailingDeleteView.as_view(), name="mailing_delete"),
    path("run/<int:pk>/", run_mailing, name="mailing_run"),
]
