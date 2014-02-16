#!/usr/bin/env python
from __future__ import unicode_literals
import sys

from django.conf import settings
from django.core.management import execute_from_command_line


if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        USE_TZ=True,
        INSTALLED_APPS=(
            'tests',
        ),
        TEST_RUNNER='django_nose.NoseTestSuiteRunner',
        NOSE_ARGS = [
            '--cover-package=arrow_field',
            '--with-coverage',
        ]
    )


def runtests():
    argv = sys.argv[:1] + ['test', 'tests']
    execute_from_command_line(argv)


if __name__ == '__main__':
    runtests()
