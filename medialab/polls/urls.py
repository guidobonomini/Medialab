from django.urls import path

from medialab.polls.views import (
    service_view
)

app_name = "polls"
urlpatterns = [
    path("polls/", view=service_view("/polls"), name="polls"),
]
