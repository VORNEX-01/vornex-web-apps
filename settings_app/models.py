from django.db import models


class SEOSettings(models.Model):

    title = models.CharField(
        max_length=200,
        default="Vornex Web App"
    )

    description = models.TextField(
        default="Modern tools platform"
    )

    keywords = models.CharField(
        max_length=300,
        blank=True
    )


    favicon = models.ImageField(
        upload_to="seo/",
        blank=True,
        null=True
    )


    def __str__(self):
        return self.title