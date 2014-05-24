# -*- coding: utf-8 -*-
#
# File: Location.py
#
# Copyright (c) 2011 by unknown <unknown>
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

from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import \
    ReferenceBrowserWidget
from Products.Newspaper.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    IntegerField(
        name='top',
        widget=IntegerField._properties['widget'](
            label='Top',
            label_msgid='Newspaper_label_top',
            i18n_domain='Newspaper',
        ),
    ),
    IntegerField(
        name='left',
        widget=IntegerField._properties['widget'](
            label='Left',
            label_msgid='Newspaper_label_left',
            i18n_domain='Newspaper',
        ),
    ),
    IntegerField(
        name='width',
        widget=IntegerField._properties['widget'](
            label='Width',
            label_msgid='Newspaper_label_width',
            i18n_domain='Newspaper',
        ),
    ),
    IntegerField(
        name='height',
        widget=IntegerField._properties['widget'](
            label='Height',
            label_msgid='Newspaper_label_height',
            i18n_domain='Newspaper',
        ),
    ),
    ReferenceField(
        name='containers',
        widget=ReferenceBrowserWidget(
            label='Containers',
            label_msgid='Newspaper_label_containers',
            i18n_domain='Newspaper',
        ),
        allowed_types=('Container',),
        multiValued=1,
        relationship='containerLocation',
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Location_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Location(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.ILocation)

    meta_type = 'Location'
    _at_rename_after_creation = True

    schema = Location_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(Location, PROJECTNAME)
# end of class Location

##code-section module-footer #fill in your manual code here
##/code-section module-footer

