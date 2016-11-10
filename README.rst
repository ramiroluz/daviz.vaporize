==============
Daviz Vaporize
==============

Daviz Vaporize provides a Word Cloud plugin for 
eea.app.visualization. See eea.daviz package for more details.


.. image:: http://eea.github.com/_images/eea.daviz.layers.svg


.. contents::


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

    zcml =
      ...
      daviz.vaporize

* Re-run buildout, e.g. with::

  $ ./bin/buildout

You can skip the ZCML slug if you are going to explicitly include the package
from another package's configure.zcml file.

Dependencies
============

`Daviz Vaporize`_ has the following dependencies:
  - Zope 2.12+
  - `eea.app.visualization`_


.. image:: http://eea.github.com/_images/eea.daviz.dependencies.svg


Source code
===========

Latest source code (Zope 2 compatible):
- `Daviz Vaporize on Github <https://github.com/ramiroluz/daviz.vaporize>`_
