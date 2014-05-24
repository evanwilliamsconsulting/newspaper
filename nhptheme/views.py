try:
    # plone.app.registry 1.0b1
    from plone.app.registry.browser.form import RegistryEditForm
    from plone.app.registry.browser.form import ControlPanelFormWrapper
except ImportError:
    # plone.app.registry 1.0b2+
    from plone.app.registry.browser.controlpanel import RegistryEditForm
    from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from plone.registry import registry

from z3c.form import form,field,button
from z3c.form.field import Fields
from plone.directives.form import EditForm
from persistent import Persistent

from Products.Archetypes.atapi import *
from Products.Archetypes.Schema import Schema
from zope.schema.fieldproperty import FieldProperty

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

from five import grok
from plone.directives import form

from zope import schema
from zope.interface import implements
from z3c.form import button

from Products.CMFCore.interfaces import ISiteRoot
from Products.statusmessages.interfaces import IStatusMessage

from interfaces import ISettings

from interfaces import Interface

from persistent import Persistent

from z3c.form import field

class ControlPanelForm(RegistryEditForm):
    label = u'Enter Issue Name'
    description = u'Provides a mechanism to link theming to a particular Issue'
    issue = FieldProperty(ISettings['issue'])
    fields = field.Fields(ISettings) 
    schema = ISettings

    @button.buttonAndHandler(u'save')
    def handlesave(self, action):
        data, errors = self.extractData()
        print data # ... or do stuff

    @button.buttonAndHandler(u'Cancel')
    def handleCancel(self, action):
        data, errors = self.extractData()
        print data # ... or do stuff
