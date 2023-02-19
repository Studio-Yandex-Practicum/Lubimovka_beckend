from django.utils import timezone
from drf_spectacular.utils import PolymorphicProxySerializer, extend_schema_field
from rest_framework import serializers

from apps.afisha.models import Event, MasterClass, Performance, Reading
from apps.afisha.serializers import EventMasterClassSerializer, EventPerformanceSerializer, EventReadingSerializer

AFISHA_EVENTS_SERIALIZER_PAIRS = {
    MasterClass: EventMasterClassSerializer,
    Performance: EventPerformanceSerializer,
    Reading: EventReadingSerializer,
}


class AfishaEventSerializer(serializers.ModelSerializer):
    """Afisha event Output serializer."""

    action_text = serializers.SerializerMethodField()
    action_url = serializers.SerializerMethodField()

    event_body = serializers.SerializerMethodField(
        help_text="The response is different based on event type.",
    )
    date_time = serializers.DateTimeField()
    opening_date_time = serializers.SerializerMethodField()

    def show_links(self, obj):
        return not self.context.get("festival_status") or timezone.now() > obj.event_day + self.context.get(
            "time_delta"
        )

    def get_action_text(self, obj):
        return obj.get_action_text_display() if self.show_links(obj) else None

    def get_action_url(self, obj):
        return obj.action_url if self.show_links(obj) else None

    def get_opening_date_time(self, obj):
        return obj.event_day + self.context.get("time_delta")

    @extend_schema_field(
        PolymorphicProxySerializer(
            component_name="Event_Type_objects",
            serializers=AFISHA_EVENTS_SERIALIZER_PAIRS.values(),
            resource_type_field_name=None,
        )
    )
    def get_event_body(self, obj):
        """Get event body type and return serialized data based on it type."""
        event_body = obj.common_event.target_model
        event_model = event_body._meta.model

        serializer_class = AFISHA_EVENTS_SERIALIZER_PAIRS[event_model]
        serializer = serializer_class(event_body, context=self.context)
        return serializer.data

    class Meta:
        model = Event
        fields = ("id", "type", "event_body", "date_time", "action_url", "action_text", "opening_date_time")
