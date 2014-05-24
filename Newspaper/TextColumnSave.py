# -*- coding: utf-8 -*-
#
# File: TextColumn.py
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
from columnar import Columnar 

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Newspaper.config import *
from Products.Newspaper.PDFPageTemplate import PDFPageTemplate

from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.units import inch

from Products.Five.browser import BrowserView
import json
##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((


    IntegerField(
        name='startLine',
        widget=IntegerField._properties['widget'](
            label='StartLine',
            label_msgid='Newspaper_label_startLine',
            i18n_domain='Newspaper',
        ),
    ),
    IntegerField(
        name='endLine',
        widget=IntegerField._properties['widget'](
            label='EndLine',
            label_msgid='Newspaper_label_endLine',
            i18n_domain='Newspaper',
        ),
    ),
    IntegerField(
        name='fontSize',
	default=11,
        widget=IntegerField._properties['widget'](
            label='fontSize',
            label_msgid='Newspaper_label_fontSize',
            i18n_domain='Newspaper',
	),
    ),
    BooleanField(
	name='useRemainder',
        widget=BooleanField._properties['widget'](
	    label='useRemainder',
	    label_msgid='Newspaper_label_useRemainder',
	    i18n_domain='Newspaper',
	),
    ),
    BooleanField(
	name='useContinuedOn',
        widget=BooleanField._properties['widget'](
	    label='useContinuedOn',
	    label_msgid='Newspaper_label_useContinuedOn',
	    i18n_domain='Newspaper',
	),
    ),
    StringField(
        name='continuedOn',
	default='Continued on Page Four',
        widget=StringField._properties['widget'](
            label='Continued On',
            label_msgid='Newspaper_label_continuedon',
            i18n_domain='Newspaper',
        ),
    ),
    BooleanField(
	name='useContinuedFrom',
        widget=BooleanField._properties['widget'](
	    label='useContinuedFrom',
	    label_msgid='Newspaper_label_useContinuedFrom',
	    i18n_domain='Newspaper',
	),
    ),
    StringField(
        name='continuedFrom',
	default='Continued From Page One',
        widget=StringField._properties['widget'](
            label='Continued From',
            label_msgid='Newspaper_label_continuedfrom',
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
    StringField(
        name='textclass',
	default='textclass',
        widget=StringField._properties['widget'](
            label='Text class',
            label_msgid='Newspaper_label_textclass',
            i18n_domain='Newspaper',
        ),
    ),
    BooleanField(
	name='glueX',
        widget=BooleanField._properties['widget'](
	    label='glueX',
	    label_msgid='Newspaper_label_glueX',
	    i18n_domain='Newspaper',
	),
    ),
    BooleanField(
	name='glueY',
        widget=BooleanField._properties['widget'](
	    label='glueY',
	    label_msgid='Newspaper_label_glueY',
	    i18n_domain='Newspaper',
	),
    ),
    BooleanField(
	name='offsetX',
        widget=BooleanField._properties['widget'](
	    label='offsetX',
	    label_msgid='Newspaper_label_offsetX',
	    i18n_domain='Newspaper',
	),
    ),
    BooleanField(
	name='resetY',
        widget=BooleanField._properties['widget'](
	    label='resetY',
	    label_msgid='Newspaper_label_resetY',
	    i18n_domain='Newspaper',
	),
    ),
    BooleanField(
	name='addLineHeight',
        widget=BooleanField._properties['widget'](
	    label='addLineHeight',
	    label_msgid='Newspaper_label_addLineHeight',
	    i18n_domain='Newspaper',
	),
    ),
    ReferenceField(
        name='wordage',
        widget=InAndOutWidget(
            label='Containers',
            label_msgid='Newspaper_label_containers',
            i18n_domain='Newspaper',
        ),
        allowed_types=('Article',),
        multiValued=1,
        relationship='containerLocation',
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

TextColumn_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema
class TextColumnJSON(BrowserView):
    """ JSON Encoded Issue """
    def __init__(self,context,request):
        """ Initialize context and request as view multiadaption parameters.

        Note that the BrowserView constructor does this for you.
        This step here is just to show how view receives its context and
        request parameter. You do not need to write __init__() for your
        views.
        """
        self.context = context
        self.request = request

    # by default call will call self.index() method which is mapped
    # to ViewPageTemplateFile specified in ZCML
    def __call__(self):
   	self.request.response.setHeader("Content-type","application/json")
	json_item = {}
	title = self.context.getId()
	json_item['TextColumn']=title
	pretty = json.dumps(json_item)    
	return pretty 

class TextColumn(BaseContent, BrowserDefaultMixin):
    """
    """
    added = False

    security = ClassSecurityInfo()

    implements(interfaces.ITextColumn)

    meta_type = 'TextColumn'
    _at_rename_after_creation = True

    schema = TextColumn_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    # Methods
    def contains(self): 
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    showTemplate=skin.showColumn
	    return showTemplate()

    def show(self): 
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

    def returnLines(self):
	    """
	    Test
	    """
	    articles = self.getWordage()
	    output = []
            for article in articles:
	    	verbage = article.getWordage()
		just = Columnar(verbage,40)
		lines = just.getLines()
		totalLines = just.countLines()
		i = 1
		while i<=totalLines:
			theLine = just.returnLine(i)
			output.append(theLine)
			i += 1
	    return output 

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
	    return self.returnLines()

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

    def getHeight(self):
            """
	    Test
	    """
	    columncontainer = '/mnt/one/newholland/press/products/Newspaper/skins/newspaper_templates/'+self.Title()
	    obj=PDFPageTemplate(self.Title(),columncontainer)
	    containerLeft = self.getLeft()
	    width = self.getCharsPerLine() * 6
	    #result=obj.continuePDF(c,x,y+30,REQUEST,parent)
	    print self.id
	    articles = self.getWordage()
	    y = 0
            for article in articles:
	    	verbage = article.getVerbage()
	        line = ""
		for char in verbage:
		    if char != '\n':
		        line += char
		    else:
			line = ""
		        y += 12
		y += 12
		y += 12
	    return y

    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top,pagenumber):
            """
	    Test
	    """
	    print self.Title()
	    xorig = x
	    yorig = y
	    xleft = self.getLeft()
	    ytop = self.getTop()
	    glueX = self.getGlueX()
            glueY = self.getGlueY()
            if glueY == True:
		y -= 50
            if glueX:
                x += xleft
	    ysave = y
	    columncontainer = '/mnt/one/newholland/press/products/Newspaper/skins/newspaper_templates/'+self.Title()
	    obj=PDFPageTemplate(self.Title(),columncontainer)
	    containerLeft = self.getLeft()
	    width = self.getCharsPerLine() * 6
	    #result=obj.continuePDF(c,x,y+30,REQUEST,parent)
	    print self.id
	    articles = self.getWordage()
	    y = 1140 - y
            for article in articles:
	    	verbage = article.getVerbage()
	        line = ""
		for char in verbage:
		    if char != '\n':
		        line += char
		    else:
		        self.drawALine(c,x,y,line)
			line = ""
		        y -= 12
		y -= 12
		self.drawALine(c,x,y,line)
		y -= 12
	    #returnTriplets = self.tripletOutput(x,y,lineSpacing)
	    #self.outputTriplets(c,returnTriplets,x,y)
	    #self.pdfOutput(c,x,y)
	    newx = x + containerLeft
	    offsetX = self.getOffsetX()
	    resetY = self.getResetY()
	    columnWidth = 4 * self.getCharsPerLine()
            if offsetX:
		returnx = x + columnWidth 
            else:
                returnx = newx + columnWidth 
	    returnx += 125
	    if resetY:
	        returny = ysave - yorig
		if self.getAddLineHeight():
			returny -= 11
	    else:
                returny = y - yorig
	    returny += 25
	    return (returnx,returny)

    def drawALine(self,c,x,y,theLine):
	    words = theLine.split()
	    totalWordLength = 0
	    for word in words:
		totalWordLength += c.stringWidth(word,"Times-Roman",16)
	    lineLength = 5 * self.getCharsPerLine()
	    #if len(words) > 1:
	    #    whiteSpace = (lineLength - totalWordLength) / (len(words) - 1)
            #else:
	    whiteSpace = 10
	    textobject = c.beginText()
	    fontSize=self.getFontSize()
	    textobject.setFont("Times-Roman",fontSize)
	    for word in words:
		stringWidth = c.stringWidth(word,"Times-Roman",fontSize)
	        textobject.setTextOrigin(x,y)
	    	textobject.textLine(word)
		x += stringWidth
		x += whiteSpace 
	    c.drawText(textobject)
            y+=4
	    return (x,y)

    def getSkinName(self):
            """
            TEST
            """
	    return "showColumn"

    def returnTextClass(self):
            """
            TEST
            """
            return self.getTextclass()

    def web(self):
	    """
	    WEB
	    """
	    articles = self.getWordage()
	    for article in articles:
		wordage = article.getWordage()
	    return wordage

    def getJSON(self):
	    """
	    TEST
	    """
	    json_item = {}
	    title = self.getId()
	    json_item['TextColumn']=title
	    json_item['elements']=super(TextColumn,self).getJSON()
	    return json_item

    def getSnapshot(self,width,height):
	    """
	    Test
	    """
	    text = "<div class='textcolumn'>"
	    articles = self.getWordage()
	    linewidth = self.getColumnWidth()
	    #linewidth = width * 1.2
	    theStyle='width:'+str(linewidth)+'px;text-align:justify;font-size:12pt'
	    for article in articles:
		theWordage = article.getWordage()
	        line = ""
		for char in theWordage:
		    if char != '\n':
		        line += char
		    else:
	    		text += "<div style='"+theStyle+"' class='textline'>"
			text += line
	    		text += "</div>"
			line = ""
	    	text += "<div style='"+theStyle+"' class='textline'>"
		text += line
	        text += "</div>"
	    text += "</div>"
	    return (text,0,0)

registerType(TextColumn, PROJECTNAME)
# end of class Column

##code-section module-footer #fill in your manual code here
##/code-section module-footer

