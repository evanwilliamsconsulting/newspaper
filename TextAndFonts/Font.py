# -*- coding: utf-8 -*-
#
# File: Font.py
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
import htmlentitydefs as entity

from Products.Five.browser import BrowserView
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Newspaper.config import *
from Products.Newspaper.PDFPageTemplate import PDFPageTemplate

from Products.Five.browser import BrowserView
import json

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='Font',
        widget=StringField._properties['widget'](
            label='Font',
            label_msgid='TextAndFonts_label_Font',
            i18n_domain='TextAndFonts',
            ),
        ),
        ),
)

Font_schema = schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema
class Font(BaseContent):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IFont)

    meta_type = 'Font'
    _at_rename_after_creation = True

    schema = Font_schema 

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(Font, PROJECTNAME)
# end of class Font

##code-section module-footer #fill in your manual code here
##/code-section module-footer
