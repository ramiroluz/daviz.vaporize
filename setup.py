# -*- coding: utf-8 -*-
"""Installer for the daviz.vaporize package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='daviz.vaporize',
    version='1.0a1',
    description="Daviz Vaporize provides a Word Cloud plugin for eea.app.visualization. See eea.daviz package for more details.",
    long_description=long_description,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Zope",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='vaporize tag word cloud Plone Zope Python',
    author='Ramiro Batista da Luz',
    author_email='ramiroluz@gmail.com',
    url='https://pypi.python.org/pypi/daviz.vaporize',
    license='GPL version 2',
    download_url="http://pypi.python.org/pypi/daviz.vaporize",
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['daviz'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.api',
        'Products.GenericSetup>=1.8.2',
        'setuptools',
        'eea.app.visualization > 9.3',
        'z3c.jbot',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            'plone.testing>=5.0.0',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
