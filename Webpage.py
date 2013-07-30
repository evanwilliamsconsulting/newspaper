# -*- coding: utf-8 -*-
#
# File: Webpage.py
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
from Products.Five.browser import BrowserView


from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics

from reportlab.pdfbase.ttfonts import TTFont

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    IntegerField(
        name='pageNo',
        widget=IntegerField._properties['widget'](
            label='Pageno',
            label_msgid='Newspaper_label_pageNo',
            i18n_domain='Newspaper',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Webpage_schema = OrderedBaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema
#class M_Webpage(NewsFolder.__class__): pass

class WebpageView(BrowserView):
   """ Available View of the Webpage. """


class Webpage(OrderedBaseFolder,ExtensibleMetadata):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IWebpage)

    meta_type = 'Webpage'
    _at_rename_after_creation = True

    schema = Webpage_schema

    #__metaclass__=M_Webpage

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header
    something = 'ferf'
    top = 0
    left = 0
    width = 0
    height = 0
    
    # Methods
    def view(self): 
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    showTemplate=skin.showWebpage
	    return showTemplate()

    security.declarePublic('show')
    def show(self): 
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    showTemplate=skin.showWebpage
	    return showTemplate()

    def listWidgets(self):
	    """
	    Test
	    """
	    items = self.listFolderContents(contentFilter={"portal_type":"Widget"})
	    return items

    def WebpageView(self):
	   """
	   Test
	   """
	   skin = self.portal_skins.newspaper_templates
	   webpageTemplate = skin.showWebpage
	   return showTemplate()

registerType(Webpage, PROJECTNAME)
# end of class Webpage

##code-section module-footer #fill in your manual code here
##/code-section module-footer

