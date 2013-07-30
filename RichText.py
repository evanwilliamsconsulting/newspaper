# -*- coding: utf-8 -*-
#
# File: RichText.py
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

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    TextField(
        name='textItem',
        widget=TextAreaWidget(
            label='Textitem',
            label_msgid='Newspaper_label_textItem',
            i18n_domain='Newspaper',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

RichText_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class RichText(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IRichText)

    meta_type = 'RichText'
    _at_rename_after_creation = True

    schema = RichText_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(RichText, PROJECTNAME)
# end of class RichText

##code-section module-footer #fill in your manual code here
##/code-section module-footer

