from django.contrib import admin
from polls.models import Poll


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    pass