#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup


setup(
    name='pybonnardel',
    version='0.1',
    long_description=open('README.rst').read(),
    description='Pybonnardel is a rapid game with multiple choice',
    author=u'François Magimel',
    url='https://github.com/psychotests/pybonnardel',
    license='GPL License',
    classifiers=[
        "Environment :: Console",
        "Environment :: X11 Applications",
        'License :: OSI Approved :: GPL License',
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python"
        "Programming Language :: Python :: 3",
        "Topic :: Games/Entertainment",
        "Topic :: Games/Entertainment :: Puzzle Games",
    ],
    platforms=['any'],
    packages=find_packages(exclude=['docs', 'tests']),
    test_suite="tests",
)
