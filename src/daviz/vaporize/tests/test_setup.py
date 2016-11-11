# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from daviz.vaporize.testing import DAVIZ_VAPORIZE_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that daviz.vaporize is properly installed."""

    layer = DAVIZ_VAPORIZE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if daviz.vaporize is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'daviz.vaporize'))

    def test_browserlayer(self):
        """Test that IDavizVaporizeLayer is registered."""
        from daviz.vaporize.interfaces import (
            IDavizVaporizeLayer)
        from plone.browserlayer import utils
        self.assertIn(IDavizVaporizeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = DAVIZ_VAPORIZE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['daviz.vaporize'])

    def test_product_uninstalled(self):
        """Test if daviz.vaporize is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'daviz.vaporize'))

    def test_browserlayer_removed(self):
        """Test that IDavizVaporizeLayer is removed."""
        from daviz.vaporize.interfaces import \
            IDavizVaporizeLayer
        from plone.browserlayer import utils
        self.assertNotIn(IDavizVaporizeLayer, utils.registered_layers())
