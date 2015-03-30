#!/usr/bin/env python
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'readme.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'lcdscreen',
    version = '0.1.0',

    description = ('A class to write to a LCD Screen using a raspberry pi'),
    long_description = long_description,
    keywords = 'raspberry pi lcd screen',

    url = 'https://github.com/mikestreety/python-screen-display',

    author = 'Mike Street',
    author_email = 'mikestreety@gmail.com',
    license = 'MIT',

    packages = find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires = ['time'],
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Development Status :: 4 - Beta',
        'Topic :: System :: Hardware',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python'
    ],
)
