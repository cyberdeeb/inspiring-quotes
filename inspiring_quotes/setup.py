# setup.py
from setuptools import setup, find_packages

setup(
    name="inspiring_quotes",
    version="0.1",
    description="A simple Python package for inspirational quotes.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
