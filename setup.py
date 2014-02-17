#!/usr/bin/env python
from __future__ import unicode_literals
from setuptools import setup, find_packages

setup(
    name='django-arrow-field',
    version='0.3.0',
    description='Django arrow datetime field',
    author='Gizmag',
    author_email='tech@gizmag.com',
    url='https://github.com/gizmag/django-arrow-field',
    packages=find_packages(),
    install_requires=['django', 'arrow']
)
