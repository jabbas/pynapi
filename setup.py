# -*- coding: utf-8 -*-
import versioneer
from setuptools import setup, find_packages

long_desc = """
cmdline tool for downloading subtitle files from various subtitle sites
(currently only napiprojekt.pl is supported)
"""

setup(
    name = "pynapi",
    author = 'Grzegorz Dzięgielewski',
    author_email = 'jabbas@jabbas.eu',
    url = "https://github.com/jabbas/pynapi",
    license = 'GPLv3',
    test_suite = 'pynapi.tests',
    use_2to3 = True,
    description = 'subtitles downloader',
    long_description = long_desc,
    entry_points = { 'console_scripts': [ 'pynapi = pynapi.cmdline:cmdline' ] },
    packages = find_packages(),
    version = versioneer.get_version(),
    cmdclass = versioneer.get_cmdclass(),
)
