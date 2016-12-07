#!/usr/bin/env python
"""
sentry-redmine
==================

An extension for Sentry which integrates with Redmine. Specifically, it allows
you to easily create Redmine tickets from events within Sentry.

:copyright: (c) 2015 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""
from setuptools import setup, find_packages


install_requires = [
    'sentry>=7.3.0',
]

setup(
    name='sentry-redmine',
    version='0.1.0',
    author='Sentry Team, Revised by Anthony DENAUD',
    author_email='support@getsentry.com',
    url='https://github.com/adenaud/sentry-redmine',
    description='A Sentry extension which integrates with Redmine.',
    long_description=__doc__,
    license='BSD',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=install_requires,
    test_suite='runtests.runtests',
    include_package_data=True,
    entry_points={
        'sentry.apps': [
            'redmine = sentry_redmine',
        ],
        'sentry.plugins': [
            'redmine = sentry_redmine.plugin:RedminePlugin'
        ],
    },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
