import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='pypatch',
      version='1.0.1',
      description='Utility to apply unified diff patches to installed python modules.',
      license='MIT',
      long_description=read('README'),
      author='Sitka Technology Group',
      include_package_data=True,
      author_email='info@sitkatech.com',
      url='http://sitkatech.com',
      packages=['pypatch', ],
      install_requires=['six'],
      keywords="build tool patch unified diff",
      entry_points={
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
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
      ])
