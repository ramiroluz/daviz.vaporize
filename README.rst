.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============
Daviz Vaporize
==============

Daviz Vaporize provides a Word Cloud plugin for 
eea.app.visualization. See eea.daviz package for more details.


.. image:: http://eea.github.com/_images/eea.daviz.layers.svg


.. contents::

Features
--------

- Based on a csv input, creates a Word/Tag Cloud visualization.
- Input csv can be data pasted in a field, a URL or a file in the portal. 


Examples
--------

TODO


Documentation
-------------

Full documentation for end users can be found in the "docs" folder.


Translations
------------

This product has not been translated yet.




Installation
============

ATTENTION, IT IS NOT WORKING YET, THE INSTRUCTIONS ABOVE ARE JUST A PLACEHOLDER BY NOW.

zc.buildout
-----------
If you are using `zc.buildout`_ and the `plone.recipe.zope2instance`_
recipe to manage your project, you can do this:

* Update your buildout.cfg file:

  * Add ``daviz.vaporize`` to the list of eggs to install
  * Tell the `plone.recipe.zope2instance`_ recipe to install a ZCML slug

  ::

    [instance]
    ...
    eggs =
      ...
      daviz.vaporize


* Re-run buildout, e.g. with::

  $ ./bin/buildout

Contribute
----------

- Issue Tracker: https://github.com/ramiroluz/daviz.vaporize/issues
- Source Code: https://github.com/ramiroluz/daviz.vaporize
- Documentation: https://github.com/ramiroluz/daviz.vaporize/docs


Dependencies
============

`Daviz Vaporize`_ has the following dependencies:
  - Zope 2.12+
  - `eea.app.visualization`_


.. image:: http://eea.github.com/_images/eea.daviz.dependencies.svg

Support
-------

If you are having issues, please let us know.
Drop an e-mail to: ramiroluz@gmail.com

Source code
===========

Latest source code (Zope 2 compatible):
- `Daviz Vaporize on Github <https://github.com/ramiroluz/daviz.vaporize>`_


The project is licensed under the GPLv2.
