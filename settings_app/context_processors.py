from .models import SEOSettings


def seo_data(request):

    seo = SEOSettings.objects.first()

    return {
        "seo": seo
    }