from django.shortcuts import render
from .models import ContentItem


def home(request):

    contents = ContentItem.objects.filter(
        is_active=True
    )

    return render(
        request,
        "home.html",
        {
            "contents": contents
        }
    )