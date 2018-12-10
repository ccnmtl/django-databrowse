import os
import sys
import django
from django.conf import settings


settings.configure(
    DEBUG=True,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'django_databrowse'
    ),
    MIDDLEWARE_CLASSES=[],
    ROOT_URLCONF='test_urls',
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
            ]
        }
    }]
)
from django.test.runner import DiscoverRunner

django.setup()

test_runner = DiscoverRunner(verbosity=1)
failures = test_runner.run_tests(['django_databrowse', ])

if failures:
    sys.exit(failures)
