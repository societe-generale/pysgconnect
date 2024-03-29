# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages

setup(
    name='pysgconnect',
    use_scm_version=True,
    packages=find_packages(),
    install_requires=['requests<=2.9.1'],
    setup_requires=[
        'setuptools_scm',
        'wheel',
    ],
    description='Utilities to interact with SGConnect'
)
