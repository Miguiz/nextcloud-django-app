from django.conf import settings

from .models.alerts import new_membership, ending_membership, changing_membership_password

NEXTCLOUD_HOST = getattr(settings, 'NEXTCLOUD_HOST', 'cloud.example.com')
NEXTCLOUD_ADMIN = getattr(settings, 'NEXTCLOUD_ADMIN', 'admin')
NEXTCLOUD_PASSWORD = getattr(settings, 'NEXTCLOUD_SECRET', 'password')

NEXTCLOUD_USE_HTTPS = getattr(settings, 'NEXTCLOUD_USE_HTTPS', True)
NEXTCLOUD_SSL_IS_SIGNED = getattr(settings, 'NEXTCLOUD_SSL_IS_SIGNED', True)

NEXTCLOUD_USER_GROUP = getattr(settings, 'NEXTCLOUD_USER_GROUP', None)
NEXTCLOUD_USER_QUOTA = getattr(settings, 'NEXTCLOUD_USER_QUOTA', '100GB')
