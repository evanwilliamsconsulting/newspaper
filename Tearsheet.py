# -*- coding: utf-8 -*-
#
# File: Tearsheet.py
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

from archetypes.referencebrowserwidget import ReferenceBrowserWidget


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
    IntegerField(
        name='pageWidth',
        widget=IntegerField._properties['widget'](
            label='Pagewidth',
            label_msgid='Newspaper_label_pageWidth',
            i18n_domain='Newspaper',
        ),
    ),


    ReferenceField(
        name='containers',
        widget=InAndOutWidget(
            label='Containers',
            label_msgid='Newspaper_label_containers',
            i18n_domain='Newspaper',
        ),
        allowed_types=('Container','YouCanBox','CreditsBox','Puzzle','Company',),
        multiValued=1,
        relationship='containerLocation',
	keepReferencesOnCopy=1,
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Tearsheet_schema = OrderedBaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema
#class M_Tearsheet(NewsFolder.__class__): pass

class Tearsheet(OrderedBaseFolder,ExtensibleMetadata):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.ITearsheet)

    meta_type = 'Tearsheet'
    _at_rename_after_creation = True

    schema = Tearsheet_schema

    #__metaclass__=M_Tearsheet

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header
    something = 'ferf'
    top = 0
    left = 0
    width = 0
    height = 0
    
    # Methods
    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top,pagenumber):
	    """
	    Test
	    """
            #textobject = c.beginText()
            #textobject.setTextOrigin(x,y)
            #textobject.setFont('FilosBold',12)
            #textobject.textLine("Tearsheet")
	    #c.drawText(textobject)
            print self.Title()
	    obj = self.getContainers()
	    for item in obj:
		item.callPDFPDTBySameName(c,x,y,REQUEST,item,top,pagenumber)
	    return (x,y)


registerType(Tearsheet, PROJECTNAME)
# end of class Tearsheet

##code-section module-footer #fill in your manual code here
##/code-section module-footer

