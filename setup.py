# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name = "pynapi",
    author = 'Grzegorz Dzięgielewski',
    author_email = 'jabbas@jabbas.eu',
    url = "https://github.com/jabbas/pynapi",
    version = '0.5.2',
    description = 'subtitles downloader',
    entry_points = { 'console_scripts': [ 'pynapi = pynapi.cmdline:cmdline' ] },
    packages = find_packages()
)
