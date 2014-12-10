#!/usr/bin/env python

"""
This is about as simple a setup.py as you can have

It installs the capitalize module and script

"""

# classic distutils
#from distutils.core import setup

## uncomment to support "develop" mode
from setuptools import setup

setup(
    name='Capitalize',
    version='0.1.0',
    author='Chris Barker',
    py_modules=['capitalize/capital_mod',],
    scripts=['scripts/cap_script.py',],
    description='Not very useful capitalizing module and script',
)

