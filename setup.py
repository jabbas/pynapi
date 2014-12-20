from setuptools import setup, find_packages

setup(
    name = "pynapi",
    version = '0.3',
    description = 'subtitles downloader',
    entry_points = { 'console_scripts': [ 'pynapi = pynapi.cmdline:cmdline' ] },
    packages = find_packages()
)
