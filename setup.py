# Setup.py

from setuptools import setup, find_packages

with open("README.md", "r") as rm:
    long_description = rm.read()

setup(
    name='lambdadata-ahviblackwell',
    version='0.0.1',
    author='Ahvi Blackwell',
    author_email='ahviblackwelldev@gmail.com',
    description='Python Package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ahvblackwelltech/lambdadata-ahvblackwell',
    keywords=['datetime', 'null value', 'pandas']
    # packages=find_packages(data)
)