from django.db import models

class CustomImageField(models.ImageField):
    def url(self):
        if self.file:
            return f"{settings.MEDIA_URL}{self.file.name}"
        return super().url()
