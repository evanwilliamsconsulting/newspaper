# -*- coding: utf-8 -*-
#
# File: Headline.py
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

from Products.Newspaper.config import *
from Products.Newspaper.PDFPageTemplate import PDFPageTemplate

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    IntegerField(
        name='lineno',
        widget=IntegerField._properties['widget'](
            label='Line No.',
            label_msgid='Newspaper_label_Lineno',
            i18n_domain='Newspaper',
        ),
    ), 
    StringField(
        name='line',
        widget=StringField._properties['widget'](
            label='Line',
            label_msgid='Newspaper_label_Line',
            i18n_domain='Newspaper',
        ),
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Line_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Line(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.ILine)

    meta_type = 'Line'
    _at_rename_after_creation = True

    schema = Line_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(Line, PROJECTNAME)
# end of class Headline

##code-section module-footer #fill in your manual code here
##/code-section module-footer

