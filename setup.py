#!/usr/bin/env python

"""
distutils/setuptools install script.
"""

from setuptools import find_packages, setup

requires = ["requests>=2.32.3", "pydantic>=2.7.4", "pycryptodome==3.21.0"]


setup(
    name="dte_colombia",
    version="0.0.1",
    description="SDK for the electronic invoicing API in Colombia by IKU Solutions",
    author="Yan Chirino",
    author_email="support@yanchirino.com",
    url="https://github.com/yanpierchirino/dte_colombia",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,  # Asegura que se incluyan los archivos adicionales
    package_data={
        "dte_colombia": [
            "stubs/*.pyi"
        ],  # Incluye los archivos .pyi dentro de la carpeta stubs
    },
    # Marca el paquete como compatible con type hints
    zip_safe=False,  # Para compatibilidad con algunas herramientas de tipado
    install_requires=requires,
    python_requires=">= 3.10.0",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    project_urls={
        "Documentation": "https://yanpierchirino.github.io/dte_colombia",
        "Source": "https://github.com/yanpierchirino/dte_colombia",
    },
)
