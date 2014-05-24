# -*- coding: utf-8 -*-
#
# File: Article.py
#
# Copyright (c) 2011 by unknown <unknown>
# Generator: ArchGenXML Version 2.6
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter

import string 
from cStringIO import StringIO

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.Five.browser import BrowserView
from zope.interface import implements
import interfaces
from columnar import Columnar

import hyphenate 

from Products.CMFCore.utils import getToolByName

from browserdefault import BrowserDefaultMixin

from Products.Newspaper.config import *

from Products.CMFCore.utils import getToolByName


from zope.component import getMultiAdapter

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    TextField(
        name='verbage',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=TextAreaWidget(
            label='Verbage',
            label_msgid='Newspaper_label_verbage',
            i18n_domain='Newspaper',
        ),
        default_output_type='text/html',
    ),
    StringField(
        name='results',
	widget=StringWidget(
		label='Results',
		label_msgid='Newspaper_label_results',
		i18n_domain='Newspaper',
	),
    ),        
    IntegerField(
        name='columnSize',
	widget=IntegerWidget(
		label='columnSize',
		label_msgid='Newspaper_label_results',
		i18n_domain='Newspaper',
	),
    ),        
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Article_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Article(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IArticle)

    meta_type = 'Article'
    _at_rename_after_creation = True

    schema = Article_schema
    containerChoice = None

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    def submitColumnChoice(self,REQUEST):
	    """
	    Test
	    """
	    # Form's select_column contains the value of the column selected.
	    catalog = getToolByName(self, 'portal_catalog')
	    items = catalog.searchResults({'portal_type': 'Column'})
	    self.columnChoice = REQUEST["select_column"]
	    for item in items:
	        if item.id==self.columnChoice:
		    column=item.getObject()
	    if column is None:
		    return
	    skin = self.portal_skins.newspaper_templates
	    submitTemplate = skin.submit
	    i = 0
	    columnSize = self.getColumnSize()
	    verbage = self.getVerbage()
	    col = Columnar(verbage,columnSize)
	    columns = col.getLines()
	    lineCount = col.countLines()
	    while i<=lineCount:
		lineid = str(i)
		if len(lineid) == 1:
		    lineid='0'+lineid
		portal_types = getToolByName(column, "portal_types")
		type_info = portal_types.getTypeInfo('Line')
		lineitem = type_info._constructInstance(column, lineid)
		lineitem.markCreationFlag()
	    	lineitem.setVerbage(columns[i])
		i+=1
	    return submitTemplate()

    def selectedColumn(self,REQUEST):
	    """
	    return Selected Column
	    """
	    selectedColumn = REQUEST["select_column"]
	    return selectedColumn

    def applyArticleToIssue(self):
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    applyIssueTemplate=skin.applyIssue
	    return applyIssueTemplate()
    
    def submitIssueChoice(self):
	    """
	    Test
	    """
	    self.issueChoice=self.REQUEST['select_issue']
    	    skin = self.portal_skins.newspaper_templates
	    #applyBroadsheetTemplate=skin.applyBroadsheet
	    #return applyBroadsheetTemplate()
	    applyContainerTemplate=skin.applyContainer
	    return applyContainerTemplate()
    
    def submitBroadsheetChoice(self):
	    """
	    Test
	    """
	    self.broadsheetChoice=self.REQUEST['select_broadsheet']
    	    skin = self.portal_skins.newspaper_templates
	    applyContainerTemplate=skin.applyContainer
	    return applyContainerTemplate()
    
    def submitContainerChoice(self):
	    """
	    Test
	    """
	    self.containerChoice=self.REQUEST['select_container']
    	    skin = self.portal_skins.newspaper_templates
	    applyColumnTemplate=skin.applyColumn
	    return applyColumnTemplate()
    
    def applyArticleToColumn(self):
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    applyColumnTemplate=skin.applyColumn
	    return applyColumnTemplate()
    
    def returnLine(self,lineid):
	    """
	    Trick
	    """
	    #Count Characters
	    lineWidth=35
	    lineStart=lineWidth*int(lineid)
	    lineEnd=lineWidth*int(lineid)+lineWidth
	    theVerbage=self.getVerbage()
	    return theVerbage[lineStart:lineEnd]

    def returnColumn(self):
	    """
	    Test
	    """
	    catalog = getToolByName(self, 'portal_catalog')
	    items = catalog.searchResults({'portal_type': 'Container'})
	    for item in items:
	        if item.id==self.containerChoice:
	    	    issue=item.getObject()
	    broadsheets = issue.getFolderContents(contentFilter={'portal_type':'Column'})
	    stringValue = "<div id='instructions'>Please select a Column for issue: "
	    stringValue += "<form method='post' action=\"/" + self.id + "/submitColumnChoice\">"
	    for broadsheet in broadsheets:
		    sheet = broadsheet.getObject()
		    stringValue += "<input type=radio name='select_column' value='%s'>%s<BR/>" % (sheet.id,sheet.Title())
	    stringValue += "<input type='submit'/>"
	    stringValue += "</form>"
	    return stringValue


    def returnBroadsheet(self):
	    """
	    Test
	    """
	    catalog = getToolByName(self, 'portal_catalog')
	    items = catalog.searchResults({'portal_type': 'Issue'})
	    for item in items:
	        if item.id==self.issueChoice:
		    issue=item.getObject()
	    broadsheets = issue.getFolderContents(contentFilter={'portal_type':'Broadsheet'})
	    stringValue = "<div id='instructions'>Please select a Broadsheet for issue: %s</div>" % issue.id
	    stringValue += "<form method='post' action=\"/" + self.id + "/submitBroadsheetChoice\">"

	    for broadsheet in broadsheets:
		    sheet = broadsheet.getObject()
		    stringValue += "<input type=radio name='select_broadsheet' value='%s'>%s<BR/>" % (sheet.id,sheet.id)
	    stringValue += "<input type='submit'/>"
	    stringValue += "</form>"
	    return stringValue

    def returnContainer(self):
	    """
	    Test
	    """
	    catalog = getToolByName(self, 'portal_catalog')
	    items = catalog.searchResults({'portal_type': 'Issue'})
	    for item in items:
	        if item.id==self.issueChoice:
		    issue=item.getObject()
	    containers = issue.getFolderContents(contentFilter={'portal_type':'Container'})
	    containers  = catalog.searchResults({'portal_type': 'Container'})
	    stringValue = "<div id='instructions'>Please select a Container for issue: %s</div>" % issue.id
	    stringValue += "<form method='post' action=\"/" + self.id + "/submitContainerChoice\">"

	    for container in containers:
		    sheet = container.getObject()
		    stringValue += "<input type=radio name='select_container' value='%s'>%s<BR/>" % (sheet.id,sheet.id)
	    stringValue += "<input type='submit'/>"
	    stringValue += "</form>"
	    return stringValue

    def returnIssue(self):
	    """
	    Test
	    """
	    catalog = getToolByName(self, 'portal_catalog')
	    items = catalog.searchResults({'portal_type': 'Issue'})
	    stringValue = "<div id='instructions'>Please select an Issue</div>"
	    stringValue += "<form method='post' action=\"/" + self.id + "/submitIssueChoice\">"
	    for item in items:
		    stringValue += "<input type=radio name='select_issue' value='%s'>%s<BR/>" % (item.id,item.Title)
	    stringValue += "<input type='submit'/>"
	    stringValue += "</form>"
	    return stringValue

    def showLines(self): 
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    showTemplate=skin.showVerbage
	    return showTemplate()

    def returnText(self):
	    """
	    Test
	    """
	    return self.getVerbage()

    def theWidth(self):
	    """
	    test
	    """
	    return "180"

    def theHeight(self):
	    """
	    Test
	    """
	    return "500"

    def getWordage(self):
	    """
	    Test
            """
            theVerbage = self.getVerbage()
	    return theVerbage

    def publish(self,REQUEST):
            """
            Publish
            """
	    skin = self.portal_skins.newspaper_templates
	    showTemplate=skin.publishVerbage
	    return showTemplate()

    def pdf(self,REQUEST): 
            """
   	    Test
            """
            skin = self.portal_skins.invoicing_templates
            showTemplate=skin.showIssue
	    output = StringIO()
	    c = canvas.Canvas(output,pagesize=letter,bottomup=0)
	    x=35
	    y=50
            textobject = c.beginText()
            textobject.setTextOrigin(x,y)
	    pdfmetrics.registerFont(TTFont('FilosBold','FilosBol.ttf'))
	    pdfmetrics.registerFont(TTFont('FilosReg','FilosReg.ttf'))
            textobject.setFont('FilosReg',14)
	    xorig = x
	    yorig = y
	    xleft = 35
	    ytop = 35
	    ysave = y
	    width = self.getColumnSize() * 6
	    verbage = self.getWordage()
	    line = ""
	    for char in verbage:
	        if char != '\n':
		    line += char
		else:
		    self.drawALine(c,x,y,line)
		    line = ""
		    y += 12
	    self.drawALine(c,x,y,line)
	    y += 12
	    newx = x + 35 
	    columnWidth = 4 * self.getColumnSize()
	    c.showPage()
	    c.save()
	    result = output.getvalue()
	    output.close()
	    response = REQUEST.RESPONSE
            response.setHeader('Content-type','application/pdf')
	    return result 

    def drawALine(self,c,x,y,theLine):
	    words = theLine.split()
	    totalWordLength = 0
	    for word in words:
		totalWordLength += c.stringWidth(word,"Times-Roman",11)
	    lineLength = 5 * self.getColumnSize()
	    #if len(words) > 1:
	    #    whiteSpace = (lineLength - totalWordLength) / (len(words) - 1)
            #else:
	    whiteSpace = 10
	    textobject = c.beginText()
	    textobject.setFont("FilosReg",11)
	    for word in words:
		stringWidth = c.stringWidth(word,"Times-Roman",11)
	        textobject.setTextOrigin(x,y)
	    	textobject.textLine(word)
		x += stringWidth
		x += whiteSpace 
	    c.drawText(textobject)
            y+=4
	    return (x,y)


    def publish(self,REQUEST):
            """
            Publish
            """
	    skin = self.portal_skins.published
	    showTemplate=skin.publishArticle
	    return showTemplate()

registerType(Article, PROJECTNAME)
# end of class Article

##code-section module-footer #fill in your manual code here
##/code-section module-footer
    
