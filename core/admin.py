from django.contrib import admin
from .models import ContentItem, SiteSettings, Announcement


@admin.register(ContentItem)
class ContentItemAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "content_type",
        "is_active"
    )


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):

    list_display = (
        "website",
    )


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "is_active",
        "created_at"
    )


    list_filter = (
        "is_active",
    )
