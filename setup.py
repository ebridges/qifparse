import os
from setuptools import setup, find_packages

version = '0.6'
long_description = open("README.md").read() + "\n" + \
    open("CHANGELOG.rst").read()

setup(name='qifparse',
      version=version,
      description="a parser for Quicken interchange format files (.qif).",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Utilities",
      ],
      keywords='qif, Quicken interchange format, file format',
      author='Giacomo Spettoli',
      author_email='giacomo.spettoli@gmail.com',
      url='https://github.com/ebridges/qifparse',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=False,
      test_suite='qifparse',
      install_requires=[
          'setuptools',
          'six',
      ],
      entry_points="""
      """,
      )
