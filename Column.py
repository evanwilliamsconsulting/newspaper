# -*- coding: utf-8 -*-
#
# File: Column.py
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
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Newspaper.config import *
from Products.Newspaper.PDFPageTemplate import PDFPageTemplate

from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.units import inch
##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((


    IntegerField(
        name='columnNo',
        widget=IntegerField._properties['widget'](
            label='Columnno',
            label_msgid='Newspaper_label_columnNo',
            i18n_domain='Newspaper',
        ),
    ),
    IntegerField(
        name='chunkSize',
        widget=IntegerField._properties['widget'](
            label='Chunksize',
            label_msgid='Newspaper_label_chunkSize',
            i18n_domain='Newspaper',
        ),
    ),
    IntegerField(
	name='charsPerLine',
	widget=IntegerField._properties['widget'](
            label='Characters per Line',
	    label_msgid='Newspaper_label_charsPerLine',
	    i18n_domain='Newspaper',
	),
    ),
    BooleanField(
	name='headline',
        widget=BooleanField._properties['widget'](
	    label='headline',
	    label_msgid='Newspaper_label_headline',
	    i18n_domain='Newspaper',
	),
    ),
    IntegerField(
	name='linesInColumn',
	widget=IntegerField._properties['widget'](
            label='Lines in Column',
	    label_msgid='Newspaper_label_linesInColumn',
	    i18n_domain='Newspaper',
	),
    ),
    FloatField(
        name='betweenLines',
        widget=FloatField._properties['widget'](
            label='Betweenlines',
            label_msgid='Newspaper_label_betweenLines',
            i18n_domain='Newspaper',
        ),
    ),
    FloatField(
        name='fontSize',
        widget=FloatField._properties['widget'](
            label='Fontsize',
            label_msgid='Newspaper_label_fontSize',
            i18n_domain='Newspaper',
        ),
    ),
    StringField(
        name='fontName',
        widget=StringField._properties['widget'](
            label='Fontname',
            label_msgid='Newspaper_label_fontName',
            i18n_domain='Newspaper',
        ),
    ),
    StringField(
        name='fontWeight',
        widget=StringField._properties['widget'](
            label='Fontweight',
            label_msgid='Newspaper_label_fontWeight',
            i18n_domain='Newspaper',
        ),
    ),
    StringField(
        name='fontClass',
        widget=StringField._properties['widget'](
            label='Fontclass',
            label_msgid='Newspaper_label_fontClass',
            i18n_domain='Newspaper',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Column_schema = OrderedBaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Column(OrderedBaseFolder, BrowserDefaultMixin):
    """
    """
    added = False

    security = ClassSecurityInfo()

    implements(interfaces.IColumn)

    meta_type = 'Column'
    _at_rename_after_creation = True

    schema = Column_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    # Methods
    def show(self): 
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    showTemplate=skin.showColumn
	    return showTemplate()

    def just(self): 
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    justTemplate=skin.justColumn
	    return justTemplate()

    def getColumnWidth(self):
    	    """
    	    TEST
    	    """
            charsPerLine = self.getCharsPerLine()
            print charsPerLine
    	    columnWidth=6*charsPerLine
    	    strColumnWidth=str(columnWidth)
    	    return strColumnWidth
    
    def getTheFontSize(self):
	    """
	    Test
	    """
	    theFontSize = self.getFontSize()
	    if None == theFontSize:
	        theFontSize = 11
	    return str(theFontSize)+'pt'

    def getLines(self):
	    """
	    Test
	    """
	    stringValue = ""
	    items = self.contentItems()
	    theLines = []
	    for item in items:
               theLines.append(item[1])
	    return theLines

    def getLinesVerbage(self):
	    """
	    Test
	    """
	    stringValue = ""
	    #items = self.listFolderContents(contentFilter={"portal_type":"Line"})
	    items = self.contentItems()
	    #theLines = []
	    for item in items:
	       stringValue += item[1].getLineVerbage()
	    return stringValue

    def getColumn(self):
	    """
	    Test
	    """
	    return self


    def listLines(self):
	    """
	    hey!
	    """
	    return self.returnInput()

    def returnInput(self):
	    """
	    Test
	    """
	    stringValue = ""
	    items = self.listFolderContents(contentFilter={"portal_type":"Line"})
	    #items = self.contentItems()
	    #for item in items:
	    #    stringValue += item[1].just()
	    #return stringValue
	    #urls=[]
	    #for item in items:
	#	if item.getHeadline() == True:
	#            urls.append(item)
	#    for item in items:
	#	if item.getHeadline() == False:
	#            urls.append(item)
	    return items

    def showHTML(self):
	    """
	    HTML
	    """
	    returnDiv=""
	    items = self.listFolderContents(contentFilter={"portal_type":"Line"})
	    for item in items:
		    theLine=item.getLineVerbage()
		    returnDiv+=theLine
	    return returnDiv

    def pdf(self):
	    """
	    Test
	    """
	    items = self.listFolderContents(contentFilter={"portal_type":"Line"})
    	    skin = self.portal_skins.newspaper_templates
	    pdfTemplate=skin.pdf
	    c=canvas.Canvas("/tmp/hello.pdf")
	    self.pdfOutput(c)
	    c.showPage()
	    c.save()
	    return pdfTemplate()

    def pdfOutput(self,c,x,y):
	    items = self.listFolderContents(contentFilter={"portal_type":"Line"})
	    for item in items:
		    theLine=item.getLineVerbage()
		    c.drawString(100,y,theLine)
		    y+=20

    def tripletOutput(self,x,y,l):
    	    triplets = []
	    items = self.listFolderContents(contentFilter={"portal_type":"Line"})
	    for item in items:
		    theLine=item.getLineVerbage()
		    triplet = (theLine,x,y)
		    y+=l
		    triplets.append(triplet)
	    return triplets
          

    def callPDTBySameName(self,REQUEST,parent,top,left,width,height,start2="",end2=""):
	    """
	    Test
	    """
	    print "Column"
	    print self.Title()
	    pathcontainer = '/opt/development/newholland/press/products/Newspaper/skins/newspaper_templates/'+self.Title()+'.pd'
	    print pathcontainer
	    result = PDFPageTemplate(self.Title(),pathcontainer)
	    fontSize=self.getFontSize()
	    fontName=self.getFontName()
	    fontWeight=self.getFontWeight()
	    fontClass=self.getFontClass()
	    charsPerLine = self.getCharsPerLine()
            width=charsPerLine*6
	    #style = "top:"
	    #style += top
	    #style += "0"
	    #style += "px;"
            style = "font-size:11pt;position:relative;"
	    style += "width:"
	    style += str(width)
            style += "px;"
            #style += "left:"
            #style += str(left)
            #style += "px;"
            style += "text-justify:inter-word;text-align:justify;float:left;margin-right:20px;"
            #style += "border-color:yellow;border-style:solid;border-width:2px;position:relative;"
	    print style
            start = "<div id='"
	    start += self.getId()
	    start += "' class='"
            start += "column"
	    start += "' style='"
	    start += style
            start += "'>"
	    end = "</div>"
            output = start
	    output += start2
	    output2 = result.continueWEB(REQUEST,parent,pathcontainer)
	    output += output2[0]
	    output += end
            height = 0
	    left = str(int(width) + int(left))
	    return (output,top,left,width,height)


    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top,pagenumber):
            """
	    Test
	    """
	    print self.Title()
	    columncontainer = '/opt/development/newholland/press/products/Newspaper/skins/newspaper_templates/'+self.Title()
	    obj=PDFPageTemplate(self.Title(),columncontainer)
	    containerLeft = parent.getLeft()
	    width = self.getCharsPerLine() * 6
	    useLeft = x
	    result=obj.continuePDF(c,useLeft,y+30,REQUEST,parent)
	    #verbage = self.getLinesVerbage()
	    #c.drawString(x,y,verbage)
	    #returnTriplets = self.tripletOutput(x,y,lineSpacing)
	    #self.outputTriplets(c,returnTriplets,x,y)
	    #self.pdfOutput(c,x,y)
	    newx = x + containerLeft 
	    return (newx,y)

registerType(Column, PROJECTNAME)
# end of class Column

##code-section module-footer #fill in your manual code here
##/code-section module-footer

