from django.contrib import admin

from apps.articles.models import NewsItem, NewsItemContent
from apps.content_pages.admin import BaseContentInline, BaseContentPageAdmin
from apps.core.mixins import StatusButtonMixin


class NewsItemContentInline(BaseContentInline):
    model = NewsItemContent

    content_type_model = (
        "imagesblock",
        "personsblock",
        "playsblock",
        "preamble",
        "quote",
        "text",
        "title",
    )


class NewsItemAdmin(StatusButtonMixin, BaseContentPageAdmin):
    inlines = (NewsItemContentInline,)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "pub_date",
                    "description",
                    (
                        "image_preview_change_page",
                        "image",
                    ),
                )
            },
        ),
    )


admin.site.register(NewsItem, NewsItemAdmin)
