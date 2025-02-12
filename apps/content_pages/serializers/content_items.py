from rest_framework import serializers

from apps.content_pages.models import EmbedCode, Link, OrderedImage, OrderedVideo
from apps.core.mixins import GetDomainMixin
from apps.core.serializers import PersonRoleSerializer
from apps.library.serializers import AuthorForPlaySerializer as LibraryPlayAuthorSerializer


class ContentUnitRichTextSerializer(serializers.Serializer):
    rich_text = serializers.CharField(
        label="Форматированный текст с HTML разметкой",
        help_text=(
            "Текст с HTML разметкой. Может содержать теги блоков: `h3`, `h4`, `p`. "
            "Блоки могут быть обернуты `blockquote` или использоваться в списках `ol`, `ul`. "
            "Разрешены теги элементов: `strong`, `em`, `a`. "
            r"Блоки разделятся последовательностью символов `\r\n\r\n`."
        ),
    )


class ExtendedPersonSerializer(serializers.Serializer):
    id = serializers.SlugRelatedField(
        source="person",
        slug_field="id",
        read_only=True,
    )
    first_name = serializers.SlugRelatedField(
        source="person",
        slug_field="first_name",
        read_only=True,
    )
    last_name = serializers.SlugRelatedField(
        source="person",
        slug_field="last_name",
        read_only=True,
    )
    middle_name = serializers.SlugRelatedField(
        source="person",
        slug_field="middle_name",
        read_only=True,
    )
    city = serializers.SlugRelatedField(
        source="person",
        slug_field="city",
        read_only=True,
    )
    email = serializers.SlugRelatedField(
        source="person",
        slug_field="email",
        read_only=True,
    )
    image = serializers.ImageField(
        source="person.image",
        read_only=True,
    )
    roles = PersonRoleSerializer(many=True)


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = (
            "title",
            "description",
            "url",
            "action_text",
        )


class EmbdedCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmbedCode
        fields = (
            "title",
            "code",
        )


class OrderedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedImage
        fields = (
            "title",
            "image",
        )


class OrderedPlaySerializer(GetDomainMixin, serializers.Serializer):
    id = serializers.IntegerField(
        source="item.id",
        label="ID",
        read_only=True,
    )
    name = serializers.CharField(
        source="item.name",
        label="Название пьесы",
        max_length=70,
    )
    authors = LibraryPlayAuthorSerializer(
        source="item.authors",
        many=True,
    )
    city = serializers.CharField(
        source="item.city",
        label="Город",
        max_length=200,
        required=False,
    )
    year = serializers.IntegerField(
        source="item.year",
        required=False,
        label="Год написания пьесы",
    )
    url_download = serializers.SerializerMethodField()
    url_reading = serializers.URLField(
        source="item.url_reading",
        label="Ссылка на читку",
        max_length=200,
    )

    def get_url_download(self, obj) -> str:
        if obj.item.url_download_from:
            return obj.item.url_download_from
        else:
            return self.prepend_domain(obj.item.url_download.url)


class OrderedVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedVideo
        fields = (
            "title",
            "url",
        )
