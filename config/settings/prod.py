"""
Django project settings for the production environment.
"""
from .base import * # noqa


ALLOWED_HOSTS = [
    '.execute-api.us-east-2.amazonaws.com',
    'senate-minutes.rjifuture.org',
]

INSTALLED_APPS = INSTALLED_APPS + ['storages',]

# default django-storages settings
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_S3_REGION_NAME = os.getenv('AWS_REGION_NAME')
AWS_AUTO_CREATE_BUCKET = True


AWS_STORAGE_BUCKET_NAME = 'senate_minutes-static'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
# BUCKET_NAME = AWS_STATIC_BUCKET_NAME
# CUSTOM_DOMAIN = AWS_STATIC_CUSTOM_DOMAIN
# BUCKET_ACL = 'public-read'
# DEFAULT_ACL = 'public-read'
# QUERYSTRING_AUTH = False
# OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# },
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
