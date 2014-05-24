# -*- coding: utf-8 -*-
#
# File: Page.py
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

Page_schema = OrderedBaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Page(OrderedBaseFolder,ExtensibleMetadata):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IPage)

    meta_type = 'Page'
    _at_rename_after_creation = True

    schema = Page_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header
    # Methods
    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top,pagenumber):
	    """
	    Test
	    """
            print self.Title()
	    containers = self.listFolderContents(contentFilter={"portal_type":"BookContainer"})
	    for container in containers:
		print container
		container.callPDFPDTBySameName(c,x,y,REQUEST,parent,top,pagenumber)
	    if pagenumber >= 10:
		realnumber = pagenumber - 9
		iterator = realnumber % 4
                if iterator == 1:
	    	    textobject = c.beginText()
	    	    fontsize = 14
	    	    textobject.setTextOrigin(x,y+fontsize)
	    	    textobject.setFont("Times-Roman", fontsize)
		    theLine = str(40-(realnumber/2))
	    	    textobject.textLine(theLine)
	    	    c.drawText(textobject)
                if iterator == 0:
	    	    textobject = c.beginText()
	    	    fontsize = 14
	    	    textobject.setTextOrigin(x,y+fontsize)
	    	    textobject.setFont("Times-Roman", fontsize)
		    theLine = str(41-(realnumber/2))
	    	    textobject.textLine(theLine)
	    	    c.drawText(textobject)
                if iterator == 2:
	    	    textobject = c.beginText()
	    	    fontsize = 14
	    	    textobject.setTextOrigin(x,y+fontsize)
	    	    textobject.setFont("Times-Roman", fontsize)
		    theLine = str((realnumber/2))
	    	    textobject.textLine(theLine)
	    	    c.drawText(textobject)
                if iterator == 3:
	    	    textobject = c.beginText()
	    	    fontsize = 14
	    	    textobject.setTextOrigin(x,y+fontsize)
	    	    textobject.setFont("Times-Roman", fontsize)
		    theLine = str(1+(realnumber/2))
	    	    textobject.textLine(theLine)
	    	    c.drawText(textobject)
	    return (x,y)

registerType(Page, PROJECTNAME)
# end of class Page

##code-section module-footer #fill in your manual code here
##/code-section module-footer

