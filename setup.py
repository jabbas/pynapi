# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name = "pynapi",
    author = 'Grzegorz Dzięgielewski',
    author_email = 'jabbas@jabbas.eu',
    url = "https://github.com/jabbas/pynapi",
    license = 'GPLv3',
    version = '0.5.3',
    description = 'subtitles downloader',
    long_description = open('README.md').read(),
    entry_points = { 'console_scripts': [ 'pynapi = pynapi.cmdline:cmdline' ] },
    packages = find_packages()
)
