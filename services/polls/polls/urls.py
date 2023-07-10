from django.contrib import admin
from django.urls import path
from polls.views import PollAPIView


app_name = "polls"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', PollAPIView.as_view()),
]