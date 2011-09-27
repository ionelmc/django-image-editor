#!/usr/bin/env python

from setuptools import setup

setup(name='django-image-editor',
    version='0.1',
    description='Allows to perform simple image editing operations in the browser window.',
    author='Millioner',
    author_email='millioner.bbb@gmail.com',
    url='https://github.com/millioner/django-image-editor',
    packages=['image_editor', ],
    include_package_data = True,    # include everything in source control
    zip_safe=False,
    install_requires=['PIL', ],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Development Status :: 4 - Beta",
        'Environment :: Web Environment',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules"
        "Framework :: Django",
        ],
    long_description = """\
Allows to perform simple image editing operations in the browser window.
"""
)
