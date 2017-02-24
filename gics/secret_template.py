DEBUG = False

ALLOWED_HOSTS = ['localhost', 'domain.tld', 'domain2.tld2']

MAIL_CHOICES = (
    ('default', 'Contacter l\'association', 'xxx@yyy.fr'),
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xxx'

MEDIA_ROOT = '/path/to/media/'

STATIC_ROOT = '/path/to/static/'

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # TODO only debug
