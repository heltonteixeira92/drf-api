from django.db import models

from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Status(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("user"),
    )

    content = models.TextField(verbose_name=_("content"))
    date_published = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Date Published")
    )
