import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='pypatch',
      version='0.5.1',
      description='Utility to apply unified diff patches to installed python modules.',
      long_description=read('README'),
      author='Sitka Technology Group',
      author_email='info@sitkatech.com',
      url='http://sitkatech.com',
      packages=['pypatch',],
      keywords="build tool patch unified diff",
      entry_points = {
          'console_scripts': [
              'pypatch = pypatch.command:main',
          ]
      },
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Topic :: Software Development :: Build Tools",
          "Topic :: Utilities",
          "Intended Audience :: Developers",
          "Natural Language :: English",
          "Programming Language :: Python :: 2.7"
      ]
)