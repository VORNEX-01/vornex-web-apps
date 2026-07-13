from django.db import models

class ContentItem(models.Model):
    TYPE_CHOICES = (

        ("webapp", "Web App"),

        ("game", "Game"),

        ("resource", "Resource"),

        ("project", "Useful Project"),

    )

    title = models.CharField(
        max_length=150
    )

    description = models.TextField()

    url = models.URLField()

    icon = models.CharField(
        max_length=200,
        blank=True
    )

    content_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default="tool"
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "محتوا"

        verbose_name_plural = "محتواها"

    def __str__(self):

        return self.title

class SiteSettings(models.Model):

    github = models.URLField(blank=True)

    instagram = models.URLField(blank=True)

    telegram = models.URLField(blank=True)

    linkedin = models.URLField(blank=True)

    website = models.URLField(blank=True)

    class Meta:
        verbose_name = "تنظیمات سایت"

        verbose_name_plural = "تنظیمات سایت"

    def __str__(self):
        return "Site Settings"

class Announcement(models.Model):

    title = models.CharField(
        max_length=200,
        verbose_name="عنوان"
    )


    message = models.TextField(
        verbose_name="متن اعلان"
    )


    link = models.URLField(
        blank=True,
        verbose_name="لینک"
    )


    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )


    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد"
    )


    class Meta:

        verbose_name = "اعلان"

        verbose_name_plural = "اعلان‌ها"



    def __str__(self):

        return self.title