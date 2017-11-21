import os
import sys

try:
	from setuptools import setup
except:
	from distutils.core import setup

dependencies = [
                   "beautifulsoup4", 
				"bs4", 
				"lxml",
				"nltk", 
				"six"
			]

def publish():
	os.system("python3 setup.py  sdist.upload")

if sys.argv[-1] == 'publish':
	publish()
	sys.exit()

setup(
	name="searchIT",
	version="0.0.1",
	description="A simple search engine in python",
	url="https://chaitya62.github.io",
	author="Chaitya Shah",
	author_email="chaitya.shah@somaiya.edu",
	install_requires=[],
	packages=['searchIT'],
	
)
