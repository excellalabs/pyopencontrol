#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = "pyopencontrol",
    description = "Generate opencontrol compliant yaml"
    version = "0.0.1",
    license = "MIT",
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords = 'opencontrol'
    packages = find_packages(),
    install_requires = [
        'openpyxl>=2.4.7',
        'wget>=3.2',
    ],
)
