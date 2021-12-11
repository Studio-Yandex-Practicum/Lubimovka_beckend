from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets

from apps.library.serializers.participation import ParticipationSerializer
from apps.library.views.auto_documentation_info import (
    ERROR_MESSAGES_FOR_PARTICIPATION_FOR_400,
)


@extend_schema(
    responses={
        201: ParticipationSerializer,
        400: ERROR_MESSAGES_FOR_PARTICIPATION_FOR_400,
    }
)
class ParticipationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ParticipationSerializer
