from django.contrib import admin
from .models import SEOSettings


@admin.register(SEOSettings)
class SEOSettingsAdmin(admin.ModelAdmin):

    list_display = (
        "title",
    )