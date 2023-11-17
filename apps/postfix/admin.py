from typing import Any

from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from apps.postfix.models import Recipient, Virtual


class RecipientsInline(admin.TabularInline):
    model = Recipient


@admin.register(Virtual)
class VirtualAdmin(admin.ModelAdmin):
    list_display = ("enabled", "author", "email", "list_recipients")
    list_display_links = ("email",)
    list_editable = ("enabled",)
    inlines = (RecipientsInline,)

    search_fields = ("author__person__first_name", "author__person__last_name", "email", "recipients__email")

    @admin.display(description="получатели")
    def list_recipients(self, obj: Virtual):
        return ", ".join(recipient.email for recipient in obj.recipients.all())

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).prefetch_related("recipients").select_related("author")
