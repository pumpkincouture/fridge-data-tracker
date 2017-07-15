try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'Making sense of refrigeration data',
        'author': 'Sylwia Bridges',
        'name': 'vaccine-data-tracker',
        'version': '0.1',
        'install_requires': ['nose']
        }

setup(**config)
