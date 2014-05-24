# -*- coding: utf-8 -*-
#
# File: Content.py
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
from Products.Newspaper.Pix import Pix
from Products.Newspaper.RichText import RichText
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Newspaper.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='author',
        widget=StringField._properties['widget'](
            label='Author',
            label_msgid='Newspaper_label_author',
            i18n_domain='Newspaper',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Content_schema = BaseSchema.copy() + \
    getattr(Pix , 'schema', Schema(())).copy() + \
    getattr(RichText, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Content(BaseContent, Pix , RichText, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IContent)

    meta_type = 'Content'
    _at_rename_after_creation = True

    schema = Content_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(Content, PROJECTNAME)
# end of class Content

##code-section module-footer #fill in your manual code here
##/code-section module-footer

