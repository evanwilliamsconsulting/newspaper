# -*- coding: utf-8 -*-
#
# File: Contact.py
#
# Copyright (c) 2012 by unknown <unknown>
# Generator: ArchGenXML Version 2.6
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

# imports needed by remember
from Products.remember.content.member import BaseMember
from Products.remember.permissions import \
        VIEW_PUBLIC_PERMISSION, EDIT_ID_PERMISSION, \
        EDIT_PROPERTIES_PERMISSION, VIEW_OTHER_PERMISSION,  \
        VIEW_SECURITY_PERMISSION, EDIT_PASSWORD_PERMISSION, \
        EDIT_SECURITY_PERMISSION, MAIL_PASSWORD_PERMISSION, \
        ADD_MEMBER_PERMISSION
from AccessControl import ModuleSecurityInfo
from Products.Invoicing.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='FirstName',
        widget=StringField._properties['widget'](
            label='Firstname',
            label_msgid='Invoicing_label_FirstName',
            i18n_domain='Invoicing',
        ),
    ),
    StringField(
        name='LastName',
        widget=StringField._properties['widget'](
            label='Lastname',
            label_msgid='Invoicing_label_LastName',
            i18n_domain='Invoicing',
        ),
    ),
    StringField(
        name='Telephone',
        widget=StringField._properties['widget'](
            label='Telephone',
            label_msgid='Invoicing_label_Telephone',
            i18n_domain='Invoicing',
        ),
    ),
    StringField(
        name='email',
        widget=StringField._properties['widget'](
            label='Email',
            label_msgid='Invoicing_label_email',
            i18n_domain='Invoicing',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Contact_schema = BaseSchema.copy() + \
    BaseMember.schema.copy() + \
    ExtensibleMetadata.schema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Contact(BaseMember, BrowserDefaultMixin, BaseContent):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IContact)

    meta_type = 'Contact'
    _at_rename_after_creation = True

    schema = Contact_schema

    base_archetype = BaseContent

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header


    # A member's __call__ should not render itself, this causes recursion
    def __call__(self, *args, **kwargs):
        return self.getId()
        

    # Methods

registerType(Contact, PROJECTNAME)
# end of class Contact

##code-section module-footer #fill in your manual code here
##/code-section module-footer

