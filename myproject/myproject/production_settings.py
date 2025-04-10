from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: define the correct hosts in production!
#ALLOWED_HOSTS = ['your-app-name.azurewebsites.net']
ALLOWED_HOSTS = ['*']

# Database settings (replace with your production database details)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Or use MySQL if you're using that
        'NAME': 'your_db_name',  # Database name
        'USER': 'your_db_user',  # Database username
        'PASSWORD': 'your_db_password',  # Database password
        'HOST': 'your_db_host',  # Database host (e.g., Azure Database URL)
        'PORT': '5432',  # PostgreSQL default port, or use 3306 for MySQL
    }
}

# Secret key for production (DO NOT use the development secret key)
# You can generate a new one using a secure random string generator.
SECRET_KEY = 'DJANGO_SECRET_KEY'

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'
import os
# Set the static files storage location
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Configure logging for production
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'django_errors.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# Set allowed CORS origins (if using CORS headers)
# CORS_ALLOWED_ORIGINS = [
#     'https://your-frontend-domain.com',
# ]

# Enable Django's built-in protection against Clickjacking
X_FRAME_OPTIONS = 'DENY'

# Enable CSRF protection in production
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# For Azure-specific settings (optional):
# If using Azure Blob Storage for media files:
# DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'

# If you are using SMTP for email in production:
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.mailtrap.io'  # Replace with your SMTP server
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your-email-username'
# EMAIL_HOST_PASSWORD = 'your-email-password'
# DEFAULT_FROM_EMAIL = 'webmaster@your-domain.com'
