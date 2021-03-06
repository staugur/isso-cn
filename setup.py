#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import io
import unittest

from setuptools import setup, find_packages

requires = ['itsdangerous', 'Jinja2', 'misaka>=2.0,<3.0', 'html5lib',
            'werkzeug>=1.0', 'bleach', 'flask-caching']

if sys.version_info < (3, ):
    raise SystemExit("Python 2 is not supported.")
elif (3, 0) <= sys.version_info < (3, 4):
    raise SystemExit("Python 3 versions < 3.4 are not supported.")


def _get_readme():
    with io.open('README.md', 'rt', encoding='utf8') as f:
        return f.read()


def test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('isso/tests', pattern='test_*.py')
    return test_suite


setup(
    name='isso-cn',
    version='0.12.3.rc2',
    author='Martin Zimmermann',
    author_email='info@posativ.org',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/staugur/isso-cn/',
    license='MIT',
    description='lightweight Disqus alternative',
    test_suite='setup.test_suite',
    long_description=_get_readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
        "Programming Language :: Python :: 3.7"
        "Programming Language :: Python :: 3.8"
    ],
    install_requires=requires,
    setup_requires=["cffi>=1.3.0"],
    entry_points={
        'console_scripts':
            ['isso = isso:main'],
    }
)
