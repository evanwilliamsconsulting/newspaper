# -*- coding: utf-8 -*-
#
# File: Correspondant.py
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
from Products.Archetypes.Schema import Schema
from Products.Archetypes.Field import *
from Products.Archetypes.Widget import *
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Newspaper.config import *
from Products.Newspaper.PDFPageTemplate import PDFPageTemplate


from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics

from reportlab.pdfbase.ttfonts import TTFont

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='username',
        widget=StringField._properties['widget'](
            label='Username',
            label_msgid='Newspaper_label_username',
            i18n_domain='Newspaper',
        ),
    ),
    StringField(
        name='handle',
        widget=StringField._properties['widget'](
            label='What\'s Your Handle',
            label_msgid='Newspaper_label_handle',
            i18n_domain='Newspaper',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Correspondant_schema = OrderedBaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema
#class M_Correspondant(NewsFolder.__class__): pass

class Correspondant(OrderedBaseFolder,ExtensibleMetadata):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.ICorrespondant)

    meta_type = 'Correspondant'
    _at_rename_after_creation = True

    schema = Correspondant_schema

    #__metaclass__=M_Correspondant

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header
    something = 'ferf'
    top = 0
    left = 0
    width = 0
    height = 0
    
    # Methods
    def show(self): 
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    showTemplate=skin.showCorrespondant
	    return showTemplate()

    def blocks(self):
	    """
	    Test
	    """
	    #blocks = self.listFolderContents(contentFilter={"portal_type":"Correspondant"})
	    blocks = self.listFolderContents(contentFilter={})
	    outputValue = ""
	    for block in blocks:
		outputValue +=  block.getId()
		outputValue += ","
	    return outputValue

registerType(Correspondant, PROJECTNAME)
# end of class Correspondant

##code-section module-footer #fill in your manual code here
##/code-section module-footer

