# -*- coding: utf-8 -*-
#
# File: LineItems.py
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

from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import  ReferenceBrowserWidget
##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    FixedPointField(
        name='Rate',
        widget=FixedPointField._properties['widget'](
            label='Rate',
            label_msgid='Invoicing_label_Rate',
            i18n_domain='Invoicing',
        ),
    ),
    IntegerField(
        name='Insertions',
        widget=IntegerField._properties['widget'](
            label='Insertions',
            label_msgid='Invoicing_label_',
            i18n_domain='Invoicing',
        ),
    ),
    FloatField(
        name='discount',
        widget=FloatField._properties['widget'](
            label='Discount',
            label_msgid='Invoicing_label_discount',
            i18n_domain='Invoicing',
        ),
    ),
    ReferenceField(
        name='advertizement',
        widget=InAndOutWidget(
            label='Advertizement',
            label_msgid='Newspaper_label_Advertizement',
            i18n_domain='Newspaper',
        ),
        allowed_types=('Advertizement',),
        multiValued=1,
        relationship='containerLocation',
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

LineItems_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class LineItems(BaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.ILineItems)

    meta_type = 'LineItems'
    _at_rename_after_creation = True

    schema = LineItems_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    def test(self):
	return "ferf"

registerType(LineItems, PROJECTNAME)
# end of class LineItems

##code-section module-footer #fill in your manual code here
##/code-section module-footer

