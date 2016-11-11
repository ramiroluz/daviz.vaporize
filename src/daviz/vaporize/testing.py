# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import daviz.vaporize


class DavizVaporizeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=daviz.vaporize)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'daviz.vaporize:default')


DAVIZ_VAPORIZE_FIXTURE = DavizVaporizeLayer()


DAVIZ_VAPORIZE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(DAVIZ_VAPORIZE_FIXTURE,),
    name='DavizVaporizeLayer:IntegrationTesting'
)


DAVIZ_VAPORIZE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(DAVIZ_VAPORIZE_FIXTURE,),
    name='DavizVaporizeLayer:FunctionalTesting'
)


DAVIZ_VAPORIZE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        DAVIZ_VAPORIZE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='DavizVaporizeLayer:AcceptanceTesting'
)
