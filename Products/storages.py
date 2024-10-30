# storages.py
from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

class MediaStorage(S3Boto3Storage):
    location = settings.AWS_LOCATION  # Set this to 'media'
    file_overwrite = False  # Prevent overwriting files with the same name

    def url(self, name):
        # Construct the full S3 URL as you want it in your database
        return f"https://{settings.AWS_S3_CUSTOM_DOMAIN}/{self.location}/{name}"
