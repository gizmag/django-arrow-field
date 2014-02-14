#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-arrow-field',
    version='0.1.1',
    description='Django arrow datetime field',
    author='Gizmag',
    author_email='tech@gizmag.com',
    url='https://github.com/gizmag/django-arrow-field',
    packages=find_packages(),
    install_requires=['django', 'arrow']
)
