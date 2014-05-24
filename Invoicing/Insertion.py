# -*- coding: utf-8 -*-
#
# File: Insertion.py
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

from Products.Invoicing.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    DateTimeField(
        name='dateOfAd',
        widget=DateTimeField._properties['widget'](
            label='Dateofad',
            label_msgid='Invoicing_label_dateOfAd',
            i18n_domain='Invoicing',
        ),
    ),
    BooleanField(
        name='notYetRun',
        widget=BooleanField._properties['widget'](
            label='Notyetrun',
            label_msgid='Invoicing_label_notYetRun',
            i18n_domain='Invoicing',
        ),
    ),
    IntegerField(
        name='page',
        widget=IntegerField._properties['widget'](
            label='Page',
            label_msgid='Invoicing_label_page',
            i18n_domain='Invoicing',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Insertion_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Insertion(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IInsertion)

    meta_type = 'Insertion'
    _at_rename_after_creation = True

    schema = Insertion_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    def test(self):
	return "ferf"

registerType(Insertion, PROJECTNAME)
# end of class Insertion

##code-section module-footer #fill in your manual code here
##/code-section module-footer

