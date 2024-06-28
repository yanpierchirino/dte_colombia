#!/usr/bin/env python

"""
distutils/setuptools install script.
"""

from setuptools import find_packages, setup


requires = [
    'requests>=2.32.3'
]


setup(
    name="dte_colombia",
    version="0.1.0",
    description="SDK for the electronic invoicing API in Colombia by IKU Solutions",
    long_description=open('README.rst').read(),
    author="Yan Chirino",
    author_email="support@yanchirino.com",
    url="https://github.com/yanchirino/dte_colombia",
    packages=find_packages(exclude=['tests*']),
    install_requires=requires,
    python_requires=">= 3.10.0",
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    project_urls={
        'Documentation': 'https://dte.yanchirino.com/v1/documentation/api/latest/index.html',
        'Source': "https://github.com/yanchirino/dte_colombia",
    },
)
