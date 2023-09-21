from setuptools import setup, Extension,find_packages

setup(
    name = 'mylib',
    packages=find_packages(where='mylib'),
    package_dir={'': 'mylib'},
)