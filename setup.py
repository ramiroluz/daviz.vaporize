""" Installer
"""
import os
from setuptools import setup, find_packages


NAME = 'daviz.vaporize'
PATH = NAME.split('.') + ['version.txt']
VERSION = open(os.path.join(*PATH)).read().strip()

setup(name=NAME,
      version=VERSION,
      description=(
          "Daviz Vaporize provides a Word Cloud plugin for EEA APP Vizualization."),
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "CHANGELOG.txt")).read(),
      classifiers=[
          "Framework :: Zope2",
          "Framework :: Zope3",
          "Framework :: Plone",
          "Framework :: Plone :: 4.0",
          "Framework :: Plone :: 4.1",
          "Framework :: Plone :: 4.2",
          "Framework :: Plone :: 4.3",
          "Programming Language :: Zope",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "License :: OSI Approved :: GNU General Public License (GPL)",
        ],
      keywords='vaporize word cloud eea plone zope python',
      author='Ramiro Batista da Luz',
      author_email="ramiroluz@gmail.com",
      maintainer='Ramiro Batista da Luz',
      maintainer_email='ramiroluz@gmail.com',
      download_url="http://pypi.python.org/pypi/daviz.vaporize",
      url='http://github.com/ramiroluz/daviz.vaporize',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['eea'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'eea.app.visualization > 9.3',
          # -*- Extra requirements: -*-
      ],
      extras_require={
          'test': [
              'plone.app.testing',
          ]
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """
      )
