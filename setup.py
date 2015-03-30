#!/usr/bin/env python
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "lcdscreen",
    version = "0.2.6",
    author = "Mike Street",
    author_email = "mikestreety@gmail.com",
    description = ("A class to write to a LCD Screen using a raspberry pi"),
    license = "BSD",
    keywords = "raspberry pi lcd screen",
    url = "https://github.com/mikestreety/python-screen-display",
    packages=['lcdscreen'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: System :: Hardware",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python"
    ],
)
