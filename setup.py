# python setup.py py2app -A

from setuptools import setup, find_packages

APP = ['main.py']
OPTIONS = {}

setup(
  app=APP,
  data_files=[],
  packages=find_packages(),
  options={'py2app': OPTIONS},
  setup_requires=['py2app'],
  install_requires = [
    'PyQt5',
    'pyqtwebengine',
    'pyspeedtest',
    'requests'
  ]
)
