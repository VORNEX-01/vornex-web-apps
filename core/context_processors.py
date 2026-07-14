from .models import ContentItem, SiteSettings, Announcement

def global_data(request):

    contents = ContentItem.objects.filter(
        is_active=True
    )


    settings = SiteSettings.objects.first()

    return {

        "contents": ContentItem.objects.filter(
            is_active=True
        ),

        "site_settings": SiteSettings.objects.first(),

        "announcement": Announcement.objects.filter(
            is_active=True
        ).first()

    }