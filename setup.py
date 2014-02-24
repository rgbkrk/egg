#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

print("*"*40)
print("What comes first, the chicken or the egg?")
print("*"*40)

setup(
    name='egg',
    version='0.2.0',
    description='This is a lonely egg.',
    long_description=readme + '\n\n' + history,
    author='Kyle Kelley',
    author_email='rgbkrk@gmail.com',
    url='https://github.com/rgbkrk/egg',
    packages=[
        'egg',
    ],
    package_dir={'egg': 'egg'},
    include_package_data=True,
    install_requires=[
        'chicken'
    ],
    license="Apache 2",
    zip_safe=False,
    keywords='egg',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)

print("*"*40)
print("On a side note, your pip syntax is probably incorrect.")
print("Are you trying to install over version control?")
print("*"*40)
