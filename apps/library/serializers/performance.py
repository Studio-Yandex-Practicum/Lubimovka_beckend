from django.db.models.query import Prefetch
from rest_framework import serializers

from apps.core.models import Role
from apps.core.serializers import ImageSerializer
from apps.library.models import Performance, TeamMember
from apps.library.utilities import team_collector

from .play import PlaySerializer


class TeamMemberSerializer(serializers.ModelSerializer):
    id = serializers.SlugRelatedField(
        source="person",
        slug_field="id",
        read_only=True,
    )
    full_name = serializers.SlugRelatedField(
        source="person",
        slug_field="full_name",
        read_only=True,
    )

    class Meta:
        model = TeamMember
        fields = (
            "id",
            "full_name",
        )


class RoleSerializer(serializers.ModelSerializer):
    persons = TeamMemberSerializer(
        source="team_members",
        read_only=True,
        many=True,
    )

    class Meta:
        model = Role
        fields = (
            "name",
            "slug",
            "persons",
        )


class PerformanceSerializer(serializers.ModelSerializer):
    """Сериализатор Спектакля для отображения на странице Спектакля."""

    play = PlaySerializer()
    team = serializers.SerializerMethodField()
    images_in_block = ImageSerializer(many=True)

    def get_team(self, obj):
        return team_collector(TeamMember, {"performance": obj})

    class Meta:
        exclude = (
            "created",
            "modified",
            "project",
            "persons",
        )
        model = Performance


class EventPerformanceSerializer(serializers.ModelSerializer):
    """Сериализатор Спектакля для отображения на странице Афиши."""

    team = serializers.SerializerMethodField()
    image = serializers.ImageField(source="main_image")
    project = serializers.SlugRelatedField(slug_field="title", read_only=True)

    def get_team(self, obj):
        performance = obj
        performance_roles = Role.objects.filter(
            team_members__performance=performance, slug__in=("director", "dramatist")
        ).distinct()
        performance_team = performance.team_members.all()
        performance_roles_with_limited_persons = performance_roles.prefetch_related(
            Prefetch(
                "team_members",
                queryset=performance_team,
            ),
        )
        serializer = RoleSerializer(
            instance=performance_roles_with_limited_persons,
            many=True,
        )
        return serializer.data
        # return team_collector(
        # TeamMember,
        # {"performance": obj, "role__slug__in": ["director", "dramatist"]},
        # )

    class Meta:
        model = Performance
        fields = (
            "id",
            "name",
            "description",
            "team",
            "image",
            "project",
        )
