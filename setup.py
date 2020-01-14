from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='rssFeeds',
    version='0.0.1',
    description='Get a torrents feed',
    long_description='TODO!!!',
    url='http://git.mlopes.space/migasll/myTorrentFeeds',
    author='Miguel Lopes',
    author_email='miguelll1991@gmail.com',
	license='MIT',
    keywords='torrent feeds',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['bs4', 'pymysql', 'guessit', 'requests', 'lxml'],
)
