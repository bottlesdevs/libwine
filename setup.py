#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='libwine',
    version='0.3',
    license='GPL-3.0',
    description='A python library for interacting with Wine.',
    keywords='libwine wine proton windows',

    url='https://github.com/bottlesdevs/libwine',

    author='Mirko Brombin',
    author_email='send@mirko.pm',

    packages=find_packages()
)
