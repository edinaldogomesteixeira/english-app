from django.contrib import admin

from .models import (
    Video,
    Vocabulary
)


admin.site.register(Video)

admin.site.register(Vocabulary)