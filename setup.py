import file_iterator
from setuptools import setup, find_packages

setup(
        name = 'file_iterator',
        version = file_iterator.__version__,
        packages = find_packages(include=['file_iterator', 'file_iterator.*'])
        )
